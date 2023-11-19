# from utils.clean_screen import clear
from rich.prompt import Prompt
from rich.console import Console
from rich.text import Text
from rich.table import Table
from email_validator import validate_email, EmailNotValidError
# from utils.password import Password
# import getpass


class UtilsUpdateUser:

    def __init__(self):
        pass

    def display_menu_update_first_name(self):
        """Vérification du prénom saisie et le controle"""
        console = Console()
        print("")
        text = (Text("Entrez le prénom souhaité :", style="blue"))
        console.print(text)
        first_name = Prompt.ask("Votre saisie >> ")

        while not (first_name.isalpha()) or not first_name:
            text = (Text("Le prénom ne peut être vide ou avec un nombre", style="red"))
            console.print(text)
            text = (Text("Entrez de nouveau un prénom :", style="red"))
            console.print(text)
            first_name = Prompt.ask("Votre nouvelle saisie >> ")

        return first_name

    def display_menu_update_last_name(self):
        """Vérification du nom saisie et le controle"""
        console = Console()
        print("")
        text = (Text("Entrez le nom souhaité :", style="blue"))
        console.print(text)
        last_name = Prompt.ask("Votre saisie >> ")

        while not (last_name.isalpha()) or not last_name:
            text = (Text("Le nom ne peut être vide ou avec un nombre", style="red"))
            console.print(text)
            text = (Text("Entrez de nouveau un nom :", style="red"))
            console.print(text)
            last_name = Prompt.ask("Votre nouvelle saisie >> ")

        return last_name

    def display_menu_update_email(self):
        """Vérification de l'adresse Email et le controle"""
        console = Console()
        print("")
        text = (Text("Entrez l'email' que vous souhaiter modifié :", style="blue"))
        console.print(text)
        email = Prompt.ask("Votre saisie >> ")

        try:
            # validate and get info
            v = validate_email(email)
            # replace with normalized form
            email = v["email"]

            return email

        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            text = (Text(str(e), style="red"))
            console.print(text)
            return UtilsUpdateUser.display_menu_email(self)

    def display_menu_update_phone(self):
        """Vérification du téléphone saisie et le controle"""
        console = Console()
        print("")
        text = (Text("Entrez le N° de téléphone à modifier :", style="blue"))
        console.print(text)
        text = (Text("Format : 0201030405", style="blue"))
        console.print(text)
        phone = Prompt.ask("Votre saisie >> ")

        if phone == "":
            return phone
        else:
            while not (phone.isnumeric()) or len(phone) > 15:
                text = (Text("Le N° de téléphone ne peut contenir de lettre ou être supérieur à 15 chiffres", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau un N° de téléphone :", style="red"))
                console.print(text)
                phone = Prompt.ask("Votre nouvelle saisie >> ")

        return phone

    def display_menu_update_phone_mobile(self):
        """Vérification du téléphone saisie et le controle"""
        console = Console()
        print("")
        text = (Text("Entrez le N° de téléphone mobile à modifier :", style="blue"))
        console.print(text)
        text = (Text("Format : 0601030405", style="blue"))
        console.print(text)
        phone_mobile = Prompt.ask("Votre saisie >> ")

        if phone_mobile == "":
            return phone_mobile
        else:
            while not (phone_mobile.isnumeric()) or len(phone_mobile) > 15:
                text = (Text("Le N° de téléphone ne peut contenir de lettre ou être supérieur à 15 chiffres", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau un N° de téléphone mobile :", style="red"))
                console.print(text)
                phone_mobile = Prompt.ask("Votre nouvelle saisie >> ")

        return phone_mobile

    def display_menu_update_role(self):
        """Modification d'un rôle à un employé"""
        print("")
        table = Table(title="Rôle de l'employé", width=80, style="green", show_lines=True)

        table.add_column("N°", style="cyan", width=10, justify="center")
        table.add_column("Rôle", style="cyan", width=70)

        table.add_row("1", "Commercial")
        table.add_row("2", "Support")
        table.add_row("3", "Gestion")
        table.add_row("4", "Aucun")

        console = Console()
        console.print(table)

        text = (Text("Entrez le numéro du rôle à affecter :", style="blue"))
        console.print(text)
        role = Prompt.ask("Votre saisie >> ")
        verify = True
        while verify:
            if role == "1":
                verify = False
                return 1
            elif role == "2":
                verify = False
                return 2
            elif role == "3":
                verify = False
                return 3
            elif role == "4":
                verify = False
                return ""
            else:
                text = (Text("La réponse saisie n'est pas correcte", style="red"))
                console.print(text)
                text = (Text("Entrez le numéro du rôle à affecter :", style="red"))
                console.print(text)
                role = Prompt.ask("Votre nouvelle saisie >> ")

    def display_menu_update_is_active(self):
        """Vérification si user saisie est actif et le controle"""
        console = Console()
        print("")
        text = (Text("L'employé est il actif :", style="blue"))
        console.print(text)
        text = (Text("   o  /  n \n", style="red"))
        console.print(text)
        is_active = Prompt.ask("Votre saisie >> ")
        verify = True
        while verify:
            if is_active.lower() == "o":
                verify = False
                return True
            elif is_active.lower() == "n":
                verify = False
                return False
            else:
                text = (Text("La réponse saisie n'est pas correcte", style="red"))
                console.print(text)
                text = (Text("   o  /  n \n", style="red"))
                console.print(text)
                is_active = Prompt.ask("Votre nouvelle saisie >> ")

        return is_active
