# What is this?

This project is a skeleton framework for building advanced command line utilities. It was developed so that it can grow
with usage. For example, you would typically start off with some lightweight utilities for automating the manual
operations in your environment. As your main project grows, your utilities project will also grow to automate more
operations within your environment. Which is why, a manageable layout is helpful.

The interface was kept separated, so that we have flexibility with distribution. In that, a separate client can be
implemented with the same interface and documentation, which may invoke the main project through a lambda function, or
lambda via api-gateway.

# How does it work?

The project is distributed in a typical MVC layout. The View in this case would be the Command Line Interface, while you
use the Model/Controller structure to organize your code based on what they do. The layout explained:

## Layout

* `model` - Data structures that represents the concepts that you're working with
* `interface` - The command line interface that the user would interact with
* `repo` - Implement Singletons for interacting with external datasets
* `resources` - Any declarative configuration files used in the project
* `service` - Reusable service class that perform the real work, in a parameterized way. Should not store data in these
  clases.
* `controller` - Handle the arguments passed in from the command line interface
* `error` - Define custom Exceptions here
* `entrypoint.py` - The default entrypoint script.
* `tests` - Unit tests for the project
* `framework` - This contains implementation to route the `interface` to the `controller`

### Entrypoint

The Entrypoint is a module inside the component directory `entrypoint.py`. It sets up the main command line interface
object. It then loads interfaces defined in `component.interface` and consolidates them as sub-commands.

### Setup

The command name can be define here. Currently, it's set to `doit` as shown in the code segment below:

```python
entry_points = '''
        [console_scripts]
        doit=component.entrypoint:cli
    '''
```

### Interface

The interface section is meant to define your interface, with associated documentation, without actually executing the
intended process or logic. This will go into a matching Controller The reason for this, is so that the interface can be
used for multiple projects, where you want the execution to be handled differently.

`component.interface.interface_one` demonstrates how to setup your interface. The interface is implemented
using [click](https://click.palletsprojects.com/)
Click provides a clean way to implement the command line interface, including options, and nested commands.

The following is an example for setting up the interface.

```python
import click

from component.framework import interface


@click.group()
def one():
    pass


@one.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
@interface
def do_stuff(count, name):
    pass

```

### Controller

The controller is the start for your implementation logic. Small commands can be fully implemented in the Controller.
Larger processes with reusable parts should be defined as reusable services.

An example controller to handle the above interface, will look like the following:

```python
from component.framework import Component


class OneController(Component):

    def do_stuff(self, name, count):
        print(f"doing it {name} {count}")

```

**Notice that the Name of the controller `OneController` matches the name of the interface group `one`. And the method
that handles the command, `do_stuff` also matches the command definition `do_stuff` under the `@one.command()`**