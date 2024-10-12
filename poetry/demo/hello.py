from rich.console import Console

from poetry.local.greeter import message


def hello_world():
    console = Console()
    console.print(message())