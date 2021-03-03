import click
from click import Group

from component.framework import load_modules

"""
This is the Entry Script, as configured in setup.py
It will initialize the main click group, and load in the interfaces from component.interface
interfaces, will then be registered as sub-commands

Each sub-command group, which is defined in the interface module, such as `component.interface.interface_one.py`
```
@click.group()
def one():
    pass
```

should be mapped to a Component Controller, named as Group-function-nameController.
for example:
OneController as found in the component.controller.cli_controller.py

All controllers would also be automatically loaded and routed to, based on the interface that was invoked.
"""


@click.group()
def cli():
    pass


def handle_groups(attribute, attribute_name):
    if isinstance(attribute, Group):
        cli.add_command(attribute)


load_modules("component.interface", handle_groups)
