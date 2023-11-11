# from utils.clean_screen import clear
from rich.prompt import Prompt
from rich.console import Console
from rich.text import Text
from email_validator import validate_email, EmailNotValidError
from utils.password import Password
import getpass


class UtilsUser:

    def __init__(self):
        pass

    def display_menu_login(self):
        """Vérification du nom de login et le controle"""
        console = Console()
        print("")
        text = (Text("Entrez le login du nouvel employé :", style="blue"))
        console.print(text)
        login = Prompt.ask("Votre saisie >> ")

        while not (login.isalpha()) or not login or len(login) > 25:
            text = (Text("Le login ne peut être vide, avec un nombre ou supérieur à 25 caractères", style="red"))
            console.print(text)
            text = (Text("Entrez de nouveau un login :", style="red"))
            console.print(text)
            login = Prompt.ask("Votre nouvelle saisie >> ")

        return login

    def display_menu_last_name(self):
        """Vérification du nom saisie et le controle"""
        console = Console()
        print("")
        text = (Text("Entrez le nom du nouvel employé :", style="blue"))
        console.print(text)
        last_name = Prompt.ask("Votre saisie >> ")

        while not (last_name.isalpha()) or not last_name:
            text = (Text("Le nom ne peut être vide ou avec un nombre", style="red"))
            console.print(text)
            text = (Text("Entrez de nouveau un nom :", style="red"))
            console.print(text)
            last_name = Prompt.ask("Votre nouvelle saisie >> ")

        return last_name

    def display_menu_first_name(self):
        """Vérification du prénom saisie et le controle"""
        console = Console()
        print("")
        text = (Text("Entrez le prénom du nouvel employé :", style="blue"))
        console.print(text)
        first_name = Prompt.ask("Votre saisie >> ")

        while not (first_name.isalpha()) or not first_name:
            text = (Text("Le prénom ne peut être vide ou avec un nombre", style="red"))
            console.print(text)
            text = (Text("Entrez de nouveau un prénom :", style="red"))
            console.print(text)
            first_name = Prompt.ask("Votre nouvelle saisie >> ")

        return first_name

    def display_menu_email(self):
        """Vérification de l'adresse Email et le controle"""
        console = Console()
        print("")
        text = (Text("Entrez l'email' du nouvel employé :", style="blue"))
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
            return UtilsUser.display_menu_email(self)

    def display_menu_phone(self):
        """Vérification du téléphone saisie et le controle"""
        console = Console()
        print("")
        text = (Text("Entrez le N° de téléphone du nouvel employé :", style="blue"))
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

    def display_menu_phone_mobile(self):
        """Vérification du téléphone Mobile saisie et le controle"""
        console = Console()
        print("")
        text = (Text("Entrez le N° de téléphone Mobile du nouvel employé :", style="blue"))
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
                text = (Text("Entrez de nouveau un N° de téléphone :", style="red"))
                console.print(text)
                phone_mobile = Prompt.ask("Votre nouvelle saisie >> ")

        return phone_mobile

    def display_menu_password(self):
        """Vérification du password saisie et le controle"""
        console = Console()
        print("")
        text = (Text("Entrez le mot de passe du nouvel employé :", style="blue"))
        console.print(text)
        text = (Text("Minimum 8 caractères :", style="red"))
        console.print(text)
        password = getpass.getpass(prompt="Votre nouvelle saisie >> ")

        while not len(password) >= 8:
            text = (Text("Le mot de passe ne peut être inférieur à 8 caractères", style="red"))
            console.print(text)
            text = (Text("Entrez de nouveau un mot de passe :", style="red"))
            console.print(text)
            password = getpass.getpass(prompt="Votre nouvelle saisie >> ")

        password_user = Password.hash_password(self, password)

        print("le mot de pass haché est ")
        print(password_user)
        return password_user

    def display_menu_is_active(self):
        """Vérification si user saisie est actif et le controle"""
        console = Console()
        print("")
        text = (Text("Le nouvel employé est il actif :", style="blue"))
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

    def display_menu_user_choice_save(self):
        """Vérification si l'utilisateur veut enregistrer l'employé'"""
        console = Console()
        verify = True
        while verify:
            print("")
            text = (Text("Confirmez la création du nouvel employé : \n", style="blue"))
            console.print(text)
            text = (Text("   o / n \n", style="red"))
            console.print(text)
            user_choice_save = input("Votre confirmation >>  ")
            if user_choice_save == "o" or user_choice_save == "n":
                verify = False

        return user_choice_save
