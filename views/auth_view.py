from rich.prompt import Prompt
from rich.console import Console
from rich.text import Text
import getpass
from utils.password import Password


class AuthView:

    def __init__(self):
        pass

    def verify_login(self, users):
        verify = True
        console = Console()
        print("")
        text = (Text("Entrez le login du nouvel employé :", style="blue"))
        console.print(text)
        login = Prompt.ask("Votre saisie >> ")
        while verify:
            for user in users:
                if user.login == login:
                    user_conected = user
                    verify = False
                    return user_conected
            else:
                text = (Text("Le login n'est pas connue dans la base de données", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau un login :", style="red"))
                console.print(text)
                login = Prompt.ask("Votre nouvelle saisie >> ")

    def verify_password(self, password_bd):
        console = Console()
        print("")
        text = (Text("Entrez le mot de passe du nouvel employé :", style="blue"))
        console.print(text)
        text = (Text("Minimum 8 caractères :", style="red"))
        console.print(text)
        password = getpass.getpass(prompt="Votre nouvelle saisie >> ")

        verify = True
        while verify:
            password_entered = Password.verify_password(self, password, password_bd)
            if password_entered == 1:
                print("Le mot de passe est correcte")
                verify = False
            else:
                text = (Text("Le mot de passe saisie n'est pas conforme", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau un mot de passe :", style="red"))
                console.print(text)
                password = getpass.getpass(prompt="Votre nouvelle saisie >> ")
