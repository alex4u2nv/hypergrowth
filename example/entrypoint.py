import click

from hypergrowth import Configuration

"""

"""


@click.group()
def cli():
    pass


Configuration(
    controllers="example.controller",
    interfaces="example.interface",
    main_command_group=cli

)
