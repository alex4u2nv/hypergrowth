import click

from component.framework import interface


@click.group()
def one():
    pass


@one.command()
@click.option('--count', default=1, help='number of greetings',
              autocompletion=[("alex", "a"), ("one", "o"), ("two", "t")])
@click.argument('name')
@interface
def do_stuff(count, name):
    pass
