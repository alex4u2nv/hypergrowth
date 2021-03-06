__version__ = "1.1.0"

from click import Group

from hypergrowth.framework import load_modules


class Configuration:

    def __init__(self,
                 controllers: str,
                 interfaces: str,
                 main_command_group: Group):
        """

        :param controllers: path to controllers `example.controller`
        :param interfaces: path to interfaces `example.interfaces`
        :param main_command_group: cli
        """

        def handle_groups(attribute, attribute_name):
            if isinstance(attribute, Group):
                main_command_group.add_command(attribute)

        load_modules(controllers, lambda *args, **kwargs: None)
        load_modules(interfaces, handle_groups)
