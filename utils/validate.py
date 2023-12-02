# from rich.prompt import Prompt
from rich.console import Console
from rich.text import Text


class Validate:
    def __init__(self):
        pass

    def validate_bd(self, text):
        console = Console()
        text = (Text(f"{text}", style="green"))
        console.print(text)
        text = (Text("Appuyer sur entrée pour revenir au menu", style="red"))
        console.print(text)
        input("")
