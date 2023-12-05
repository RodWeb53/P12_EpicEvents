from utils.client import UtilsClient
from controllers.auth_controller import AuthController
from utils.clean_screen import clear
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text


class ClientView:

    def __init__(self):
        self.utils_client = UtilsClient

    def new_client(self, token):
        auth = AuthController.decrypt_token(self, token)
        change = "du nouveau client"
        new_client_add = {}
        create_entry = True
        while create_entry:
            client_last_name = self.utils_client.display_menu_last_name(self, change)
            client_first_name = self.utils_client.display_menu_first_name(self, change)
            full_name = f"{client_last_name} - {client_first_name}"
            email = self.utils_client.display_menu_email(self, change)
            phone = self.utils_client.display_menu_phone(self, change)
            company_name = self.utils_client.display_menu_company_name(self, change)
            choice_user = self.utils_client.display_menu_client_choice_save(self)
            create_entry = False
        if choice_user == "o":
            new_client_add = {
                "full_name": str(full_name),
                "email": str(email),
                "phone": str(phone),
                "company_name": str(company_name),
                "commercial_id": auth["id"]
            }
            return new_client_add
        elif choice_user == "n":
            return -1

    def view_clients(self, clients):
        """Affichage des clients"""
        clear()
        print("")
        table = Table(title="Liste des clients", width=110, style="blue", show_lines=True)

        table.add_column("N°", style="cyan", width=10, justify="center")
        table.add_column("Nom entreprise", style="cyan", width=40)
        table.add_column("Nom commercial", style="cyan", width=30)
        table.add_column("Prénom commercial", style="cyan", width=30)

        for client in clients:
            table.add_row(f"{client.client_id}",
                          f"{client.company_name}",
                          f"{client.contact_commercial.first_name}",
                          f"{client.contact_commercial.last_name}")

        console = Console()
        console.print(table)

    def view_one_client(self, client):
        clear()
        print("")
        table = Table(title=f"Information sur le client : {client.full_name}", width=80, style="blue", show_lines=True)

        table.add_column("Caractéristique", style="cyan", width=30, justify="center")
        table.add_column("Valeur", style="cyan", width=50)

        table.add_row("Nom entreprise", f"{client.company_name}")
        table.add_row("Nom complet", f"{client.full_name}")
        table.add_row("Email", f"{client.email}")
        table.add_row("Teléphone", f"{client.phone}")
        table.add_row("Date de création", f"{client.creation_date}")
        table.add_row("Date de mise à jour", f"{client.update_date}")
        table.add_row("Contact commercial", f"{client.contact_commercial.last_name}")

        console = Console()
        console.print(table)

    def choice_user(self, clients):
        console = Console()
        list_clients = []
        text = (Text("Entrez le N° de client que vous souhaitez afficher :", style="blue"))
        console.print(text)
        choice = Prompt.ask("Votre saisie >> ")
        create_entry = True
        for client in clients:
            list_clients.append(client.client_id)
        while create_entry:
            if choice.isnumeric():
                if int(choice) in list_clients:
                    create_entry = False
                    return choice
                else:
                    text = (Text("Le numéro du client saisie n'est pas connue dans la base de données ", style="red"))
                    console.print(text)
                    text = (Text("Entrez de nouveau un numéro :", style="red"))
                    console.print(text)
                    choice = Prompt.ask("Votre nouvelle saisie >> ")
            else:
                text = (Text("Le N° de client ne peut contenir de lettre ou vide", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau le N° du client souhaité :", style="red"))
                console.print(text)
                choice = Prompt.ask("Votre nouvelle saisie >> ")
