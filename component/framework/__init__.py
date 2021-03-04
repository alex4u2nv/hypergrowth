import copy
import functools
import hashlib
import inspect
import logging
from importlib import import_module
from inspect import isclass
from pathlib import Path
from pkgutil import iter_modules

import click

package = {
    "controller": "component.controller"
}


class Qualifier:
    def __init__(self):
        self._data: str = None

    def get(self, key):
        return self._data.get(key)

    def get_md5(self):
        md5 = hashlib.md5()
        md5.update(self._data.encode("UTF-8"))
        return md5.hexdigest().lower()

    def __getitem__(self, key):
        return self._data[key]

    def __str__(self):
        if not self._data:
            raise AttributeError("Qualifier is Empty")
        return self.get_md5()

    class Builder:
        __qualifier: 'Qualifier'

        def __init__(self):
            self.__qualifier = None

        def set_name(self, name) -> 'Qualifier.Builder':
            self.__qualifier._data = name
            return self

        def build(self, name=None) -> 'Qualifier':
            qualifier = Qualifier()
            if name:
                qualifier._data = name
                return qualifier
            if not self.__qualifier._data:
                raise AttributeError("Qualifier attributes cannot be empty")
            return copy.deepcopy(self.__qualifier)


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
        qualifier: Qualifier = (Qualifier
                                .Builder()
                                .build(qualifier_str))
        return f"{cls.__name__}_{qualifier.get_md5()}", qualifier

    @classmethod
    def instance(cls, clz=None, qualifier="default", **kwargs):
        """

        :param args:
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
        handler = getattr(globals().get(ctrl).instance(),
                          str(tokenize_command_path[2]).replace("-", "_"))
        handler(**kwargs)

    return functools.update_wrapper(run, f)
