import click

from component.framework import interface


@click.group()
def two():
    pass


@two.command()
@interface
def do_other_stuff():
    pass
