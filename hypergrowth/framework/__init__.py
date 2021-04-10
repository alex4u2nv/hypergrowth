import copy
import functools
import hashlib
import inspect
import logging
import os
import uuid
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import EnumMeta, Enum
from importlib import import_module
from inspect import isclass
from pathlib import Path
from pkgutil import iter_modules

import click
from awslambdaric.lambda_context import LambdaContext


@dataclass(frozen=True)
class Qualifier:
    """
    Use this qualifier for designating a unique object
    """
    name: str
    md5: str = field(init=False)

    def get_md5(self):
        return self.md5

    def __post_init__(self):
        md5 = hashlib.md5()
        md5.update(self.name.encode("UTF-8"))
        object.__setattr__(self, "md5", md5.hexdigest().lower())


class Component:
    """
    Inheriting this class provides a factory to get a consistent single named instance when invoking the
    .instance method
    otherwise, if using the constructor, you will get a unique object
    """
    _instances = {}
    __qualifier: Qualifier

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def __get_instance_id(cls, qualifier_str):
        qualifier: Qualifier = (Qualifier(qualifier_str))
        return f"{cls.__name__}_{qualifier.get_md5()}", qualifier

    @classmethod
    def instance(cls, clz=None, qualifier="default", **kwargs):
        """

        :param clz: Allow overriding the .instance() , and passing custom class
        :param qualifier: the name for this instance
        :param kwargs:
        :return:
        """
        logging.debug(qualifier)
        args: inspect.ArgInfo = copy.deepcopy(inspect.getargvalues(inspect.currentframe()))
        items = {**args.locals, **kwargs}
        int_kwargs = {}
        [int_kwargs.update({k: v}) for k, v in items.items() if k != "cls" and k != "clz" and k != 'kwargs' and v]
        instance_id, q = cls.__get_instance_id(qualifier)
        the_class = clz if clz else cls
        if instance_id in cls._instances.keys():
            return cls._instances[instance_id]
        cls._instances[instance_id] = the_class(**int_kwargs)
        return cls._instances[instance_id]


def load_modules(package, handle):
    # iterate through the modules in the current package
    module = __import__(package, fromlist=['object'])
    package_dir = Path(module.__file__).resolve().parent
    for (_, module_name, _) in iter_modules([package_dir]):
        # import the module and iterate through its attributes
        module = import_module(f"{package}.{module_name}")
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            handle(attribute=attribute, attribute_name=attribute_name)

            if isclass(attribute):
                # Add the class to this package's variables
                globals()[attribute_name] = attribute


os.environ = {
    "AWS_LAMBDA_FUNCTION_NAME": "local-client",
}


def interface(f):
    """
    Use this to define click interfaces that could be portable to different clients
    :param f:
    :return:
    """

    @click.pass_context
    def run(ctx, *args, **kwargs):
        tokenize_command_path = ctx.command_path.split(' ')
        ctrl = f"{tokenize_command_path[1].capitalize()}Controller"
        try:
            handler = getattr(globals().get(ctrl).instance(),
                              str(tokenize_command_path[2]).replace("-", "_"))
            cli_context: LambdaContext = LambdaContext(
                invoke_id=f"client-{uuid.uuid4().hex}",
                client_context={},
                cognito_identity={},
                epoch_deadline_time_in_ms=int(datetime.now().timestamp() * 1000),
                invoked_function_arn="arn:local:client",
            )
            handler(**kwargs, context=cli_context)
        except AttributeError as ae:
            logging.fatal(f"Could not find controller {ctrl}")
            raise

    return functools.update_wrapper(run, f)


class ABCEnumMeta(ABCMeta, EnumMeta):
    pass


class GeneralEnum(Enum, metaclass=ABCEnumMeta):
    """
    General Enum with method to get a list of all values
    """

    @classmethod
    def values(cls):
        return list(map(lambda x: x.value, cls))


class DefaultEnum(GeneralEnum):
    """
    An Enum type that will return a default. useful for defining commands
    """

    @classmethod
    @abstractmethod
    def default(cls) -> Enum:
        pass

    @classmethod
    def default_value(cls):
        return cls.default().value
