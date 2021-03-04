import os

import click
from click import Group

from component.framework import load_modules

"""

"""



@click.group()
def cli():
    pass


def handle_groups(attribute, attribute_name):
    if isinstance(attribute, Group):
        cli.add_command(attribute)


load_modules("component.controller", lambda *args, **kwargs: None)
load_modules("component.interface", handle_groups)
