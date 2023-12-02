from rich.prompt import Prompt
from rich.console import Console
from rich.text import Text
from email_validator import validate_email, EmailNotValidError


class UtilsClient:

    def __init__(self):
        pass

    def display_menu_last_name(self, change):
        """Vérification du nom saisie et le controle"""
        console = Console()
        print("")
        text = (Text(f"Entrez le nom {change} :", style="blue"))
        console.print(text)
        last_name = Prompt.ask("Votre saisie >> ")

        while not (last_name.isalpha()) or not last_name:
            text = (Text("Le nom ne peut être vide ou avec un nombre", style="red"))
            console.print(text)
            text = (Text("Entrez de nouveau un nom :", style="red"))
            console.print(text)
            last_name = Prompt.ask("Votre nouvelle saisie >> ")

        return last_name

    def display_menu_first_name(self, change):
        """Vérification du prénom saisie et le controle"""
        console = Console()
        print("")
        text = (Text(f"Entrez le prénom {change} :", style="blue"))
        console.print(text)
        first_name = Prompt.ask("Votre saisie >> ")

        while not (first_name.isalpha()) or not first_name:
            text = (Text("Le prénom ne peut être vide ou avec un nombre", style="red"))
            console.print(text)
            text = (Text("Entrez de nouveau un prénom :", style="red"))
            console.print(text)
            first_name = Prompt.ask("Votre nouvelle saisie >> ")

        return first_name

    def display_menu_email(self, change):
        """Vérification de l'adresse Email et le controle"""
        console = Console()
        print("")
        text = (Text(f"Entrez l'email' {change} :", style="blue"))
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
            return UtilsClient.display_menu_email(self)

    def display_menu_phone(self, change):
        """Vérification du téléphone saisie et le controle"""
        console = Console()
        print("")
        text = (Text(f"Entrez le N° de téléphone {change} :", style="blue"))
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

    def display_menu_company_name(self, change):
        """Vérification du nom de l'entreprise'"""
        console = Console()
        print("")
        text = (Text(f"Entrez le nom de l'entreprise {change} :", style="blue"))
        console.print(text)
        company_name = Prompt.ask("Votre saisie >> ")

        while company_name == "":
            text = (Text("Le nom ne peut être vide", style="red"))
            console.print(text)
            text = (Text("Entrez de nouveau un nom :", style="red"))
            console.print(text)
            company_name = Prompt.ask("Votre nouvelle saisie >> ")

        return company_name

    def display_menu_client_choice_save(self):
        """Vérification si l'utilisateur veut enregistrer le client'"""
        console = Console()
        verify = True
        while verify:
            print("")
            text = (Text("Confirmez la création du nouveau client : \n", style="blue"))
            console.print(text)
            text = (Text("   o / n \n", style="red"))
            console.print(text)
            user_choice_save = input("Votre confirmation >>  ")
            if user_choice_save == "o" or user_choice_save == "n":
                verify = False

        return user_choice_save
