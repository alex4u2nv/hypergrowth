# ℹ️ What is this?

This project is a skeleton framework for building advanced command line utilities. It was developed so that it can grow
with usage. For example, you would typically start off with some lightweight utilities for automating the manual
operations in your environment. As your main project grows, your utilities project will also grow to automate more
operations within your environment. Which is why, a manageable layout is helpful.

The interface was kept separated, so that we have flexibility with distribution. In that, a separate client can be
implemented with the same interface and documentation, which may invoke the main project through a lambda function, or
lambda via api-gateway.

# ❔ How does it work?

The project is distributed in a typical MVC layout. The View in this case would be the Command Line Interface, while you
use the Model/Controller structure to organize your code based on what they do. The layout explained:

## 💠 Layout

#### 🌴 hypergrowth

📂 `framework` - This contains implementation to route the `interface` to the `controller`.  

#### 💡 example

🟡 `model` - Data structures that represents the concepts that you're working with.  
🗄️ `repo` - Implement Singletons for interacting with external datasets.  
📜 `resources` - Any declarative configuration files used in the project.  
⚙️  `service` - Reusable service class that perform the real work, in a parameterized way. Should not store data in these
  classes.  
🎛️ `controller` - Handle the arguments passed in from the command line interface.  
⚠️ `error` - Define custom Exceptions here.  
🟢 `entrypoint.py` - The default entrypoint script.  
🧪 `tests` - Unit tests for the project.  

#### 👐 example_shared

This project you will share among all your projects. So that they can all inherit the same Command line interface, even
though, execution may be different. In that, your first project would execute directly, whereas, your distributed
project may execute through a lambda or api-gateway interface

🤝 `interface` - The command line interface that the user would interact with.  

### 🟢 Entrypoint

The Entrypoint is a module inside the example directory `entrypoint.py`. It sets up the main command line interface
object. It then loads interfaces defined in `example.interface` and consolidates them as sub-commands.

### 🏗️ Setup

The command name can be define here. Currently, it's set to `doit` as shown in the code segment below:

```python
entry_points = '''
        [console_scripts]
        hg=example.entrypoint:cli
    '''
```

### 🤝 Interface

The interface section is meant to define your interface, with associated documentation, without actually executing the
intended process or logic. This will go into a matching Controller The reason for this, is so that the interface can be
used for multiple projects, where you want the execution to be handled differently.

`example.interface.interface_one` demonstrates how to setup your interface. The interface is implemented
using [click](https://click.palletsprojects.com/)
Click provides a clean way to implement the command line interface, including options, and nested commands.

The following is an example for setting up the interface.

```python
import click

from hypergrowth import Configuration


@click.group()
def cli():
    pass


Configuration(
    controllers="example.controller",
    interfaces="example.interface",
    main_command_group=cli

)


```

### 🎛️ Controller

The controller is the start for your implementation logic. Small commands can be fully implemented in the Controller.
Larger processes with reusable parts should be defined as reusable services.

An example controller to handle the above interface, will look like the following:

```python
from hypergrowth.framework import Component


class OneController(Component):

    def do_stuff(self, name, count, context):
        print(f"doing it {name} {count}")

```

** Notice that the Name of the controller `OneController` matches the name of the interface group `one`. And the method
that handles the command, `do_stuff` also matches the command definition `do_stuff` under the `@one.command()`.

In addition to these arguments, an extra required context argument is required. This will contain context information
relating to the execution. For local execution, the function name will be local-cli; however, when deployed as a Lambda 
function, it will be that of the function name.
**

# Requirements
## Local Shell Utility
* **Python >= 3.8** -- https://www.python.org/downloads/
* **tox** -- https://tox.readthedocs.io/en/latest/install.html

## Local AWS SAM Testing
* **sam** -- https://aws.amazon.com/serverless/sam/
* **docker** -- https://docs.docker.com/get-docker/

# ℹ️ Usage
## Local
* activate your python venv `python3 -m venv path-to-env; source path-to-env/bin/activate`
* install the framework with examples: `pip3 install hypergrowth`
* Test the example command `hgex one do-stuff jump`. This should print `doing it jump 1`
* Follow the `example` and `example_shared` examples structure in the github project, to implement your own project 
* Optionally, activate shell for [auto-completion](https://click.palletsprojects.com/en/7.x/bashcomplete/)

## Lambda Via SAM
* build `docker` image via `sam build`
* configure an `events.json` for testing, using the example in `events/events.json`
* execute via `sam local invoke -e events/events.json`

# ℹ️ Additional Notes
### 💻 Autocompletion for Big Sur zsh shell

Auto completion for the zsh shell doesn't work right of the bat. The easiest way for me to get this working, was to
install `zsh-completion`
via `brew info zsh-completions`
Then adding the following to `.zshrc`

```shell
if type brew &>/dev/null; then
    FPATH=$(brew --prefix)/share/zsh-completions:$FPATH

    autoload -Uz compinit
    compinit
fi

#HG and hg is based on your configuration in the setup.py
eval "$(_HGEX_COMPLETE=source_zsh hgex)"  
```
