from utils.client import UtilsClient
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from utils.clean_screen import clear


class UpdateClientView:

    def __init__(self):
        self.utils_client = UtilsClient

    def update_full_name(self):
        """Modification du full_name du client"""
        change = "du client modifié "
        client_last_name = UtilsClient.display_menu_last_name(self, change)
        client_first_name = UtilsClient.display_menu_first_name(self, change)
        full_name = f"{client_last_name} - {client_first_name}"
        return full_name

    def update_email(self):
        """Modifiaction de email"""
        change = "du client modifié "
        update_email = UtilsClient.display_menu_email(self, change)
        return update_email

    def update_phone(self):
        """Modifiaction du téléphone"""
        change = "du client modifié "
        update_phone = UtilsClient.display_menu_phone(self, change)
        return update_phone

    def update_company_name(self):
        """Modifiaction du du nom de l'entreprise"""
        change = "du client modifié "
        update_company_name = UtilsClient.display_menu_company_name(self, change)
        return update_company_name

    def view_commerciaux(self, users):
        """Liste des commerciaux de l'entreprise"""
        clear()
        print("")
        table = Table(title="Liste des commerciaux", width=80, style="blue", show_lines=True)

        table.add_column("N°", style="cyan", width=10, justify="center")
        table.add_column("Nom", style="cyan", width=40)
        table.add_column("Prénom", style="cyan", width=40)

        for user in users:
            table.add_row(f"{user.id}", f"{user.last_name}", f"{user.first_name}")

        console = Console()
        console.print(table)

    def choice_user(self, clients):
        """Module pour connaitre le client à modifier et vérifier s'il est dans la liste"""
        console = Console()
        list_clients = []
        text = (Text("Entrez le N° de client que vous souhaitez modifier :", style="blue"))
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

    def choice_commercial(self, users):
        """Module pour connaiitre le commercial à affecter et vérifier qu'il est dans la liste"""
        console = Console()
        list_commerciaux = []
        text = (Text("Entrez le N° de commercial que vous souhaitez affecter :", style="blue"))
        console.print(text)
        choice = Prompt.ask("Votre saisie >> ")
        create_entry = True
        for user in users:
            list_commerciaux.append(user.id)
        while create_entry:
            if choice.isnumeric():
                if int(choice) in list_commerciaux:
                    create_entry = False
                    return choice
                else:
                    text = (Text("Le numéro du commercial saisie n'est pas connue dans la base de données ", style="red"))
                    console.print(text)
                    text = (Text("Entrez de nouveau un numéro :", style="red"))
                    console.print(text)
                    choice = Prompt.ask("Votre nouvelle saisie >> ")
            else:
                text = (Text("Le N° du commercial ne peut contenir de lettre ou vide", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau le N° du commercial souhaité :", style="red"))
                console.print(text)
                choice = Prompt.ask("Votre nouvelle saisie >> ")
