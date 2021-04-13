import click
from click import Group
from click.testing import CliRunner

from hypergrowth.framework import load_modules


@click.group()
def cli():
    pass


def handle_groups(attribute, attribute_name):
    if isinstance(attribute, Group):
        cli.add_command(attribute)


load_modules("example_shared.interface", handle_groups)


def test_interface():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert "one" in result.stdout

    result = runner.invoke(cli, ["one"])
    assert "do-stuff" in result.stdout

    result = runner.invoke(cli, ["one", "do-stuff", "alex"])
    assert "" == result.stdout

