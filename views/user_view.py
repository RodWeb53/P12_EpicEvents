from utils.user import UtilsUser
from utils.clean_screen import clear
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text


class AddUserView:

    def __init__(self):
        self.utils_user = UtilsUser

    def new_user(self):
        new_user_add = {}
        create_entry = True
        clear()

        while create_entry:
            login = self.utils_user.display_menu_login(self)
            last_name = self.utils_user.display_menu_last_name(self)
            first_name = self.utils_user.display_menu_first_name(self)
            email = self.utils_user.display_menu_email(self)
            phone = self.utils_user.display_menu_phone(self)
            phone_mobile = self.utils_user.display_menu_phone_mobile(self)
            password = self.utils_user.display_menu_password(self)
            is_staff = False
            role = self.utils_user.display_menu_role(self)
            is_active = self.utils_user.display_menu_is_active(self)
            choice_user = self.utils_user.display_menu_user_choice_save(self)
            create_entry = False
        if choice_user == "o":
            new_user_add = {
                "login": str(login),
                "last_name": str(last_name),
                "first_name": str(first_name),
                "email": str(email),
                "phone": str(phone),
                "phone_mobile": str(phone_mobile),
                "password": str(password),
                "role_id": int(role),
                "is_staff": is_staff,
                "is_active": is_active,
            }
            return new_user_add
        elif choice_user == "n":
            return -1


class EditUserView:

    def __init__(self):
        self.utils_user = UtilsUser

    def view_users(self, users):
        clear()
        print("")
        table = Table(title="Liste des utilisateurs", width=80, style="blue", show_lines=True)

        table.add_column("N°", style="cyan", width=10, justify="center")
        table.add_column("Nom", style="cyan", width=40)
        table.add_column("Prénom", style="cyan", width=40)

        for user in users:
            table.add_row(f"{user.id}", f"{user.last_name}", f"{user.first_name}")

        console = Console()
        console.print(table)

    def view_one_user(self, user):
        clear()
        print("")
        table = Table(title="Information employé", width=80, style="blue", show_lines=True)

        table.add_column("Caractéristique", style="cyan", width=30, justify="center")
        table.add_column("Valeur", style="cyan", width=50)

        table.add_row("Nom", f"{user.last_name}")
        table.add_row("Prénom", f"{user.first_name}")
        table.add_row("Email", f"{user.email}")
        table.add_row("Tel fixe", f"{user.phone}")
        table.add_row("Tel mobile", f"{user.phone_mobile}")

        console = Console()
        console.print(table)
        return 0

    def choice_user(self):
        console = Console()
        text = (Text("Entrez le N° de l'employé que vous souhaitez afficher :", style="blue"))
        console.print(text)
        choice = Prompt.ask("Votre saisie >> ")
        return choice
