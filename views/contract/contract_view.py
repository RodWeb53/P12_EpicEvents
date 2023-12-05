from utils.contract import UtilsContract
from utils.clean_screen import clear
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text


class ContractView:

    def __init__(self):
        self.utils = UtilsContract

    def add_contract(self, token, clients):
        print("dans la vue de contrat")
        new_contract_add = {}
        change = "du nouveau contrat"
        create_entry = True
        while create_entry:
            contract_amount = self.utils.display_contract_amount(self, change)
            due_payment = self.utils.display_contract_due_payment(self, change)
            contract_status = self.utils.display_menu_status_contract(self)
            client_id = self.utils.display_menu_choice_client(self, clients)
            # Demande confirmation de création
            choice_user = self.utils.display_menu_contract_choice_save(self)
            create_entry = False
        if choice_user == "o":
            new_contract_add = {
                "contract_amount": float(contract_amount),
                "due_payment": float(due_payment),
                "contract_status": contract_status,
                "client_id": str(client_id),
            }
            print("les données de new_contract")
            return new_contract_add
        elif choice_user == "n":
            return -1

    def view_contracts(self, contracts):
        """Affichages de tous les contrats"""
        clear()
        clear()
        print("")
        table = Table(title="Liste des contrats", width=110, style="blue", show_lines=True)

        table.add_column("N°", style="cyan", width=10, justify="center")
        table.add_column("Nom entreprise", style="cyan", width=50)
        table.add_column("Contact client", style="cyan", width=50)

        for contract in contracts:
            table.add_row(f"{contract.contract_id}",
                          f"{contract.client.company_name}",
                          f"{contract.client.full_name}",)

        console = Console()
        console.print(table)

    def view_one_contract(self, contract):
        clear()
        print("")
        table = Table(title=f"Information sur le contrat N° : {contract.contract_id}",
                      width=80, style="blue", show_lines=True)

        table.add_column("Caractéristique", style="cyan", width=30, justify="center")
        table.add_column("Valeur", style="cyan", width=50)

        table.add_row("Nom entreprise", f"{contract.client.company_name}")
        table.add_row("Contact client", f"{contract.client.full_name}")
        table.add_row("Email", f"{contract.client.email}")
        table.add_row("Teléphone", f"{contract.client.phone}")
        table.add_row("Contact commercial", f"{contract.client.contact_commercial.last_name}")
        table.add_row("Montant du contrat", f"{contract.contract_amount}")
        table.add_row("Montant restant à payer", f"{float(contract.contract_amount - contract.due_payment)}")
        if contract.contract_status:
            table.add_row("Contrat signé", "Oui")
        else:
            table.add_row("Contrat signé", "Non")
        table.add_row("Date de création", f"{contract.creation_date}")

        console = Console()
        console.print(table)

    def choice_user(self, contracts):
        console = Console()
        list_contracts = []
        text = (Text("Entrez le N° de contrat que vous souhaitez afficher :", style="blue"))
        console.print(text)
        choice = Prompt.ask("Votre saisie >> ")
        create_entry = True
        for contract in contracts:
            list_contracts.append(contract.contract_id)
        while create_entry:
            if choice.isnumeric():
                if int(choice) in list_contracts:
                    create_entry = False
                    return choice
                else:
                    text = (Text("Le numéro du client saisie n'est pas connue dans la base de données ", style="red"))
                    console.print(text)
                    text = (Text("Entrez de nouveau un numéro :", style="red"))
                    console.print(text)
                    choice = Prompt.ask("Votre nouvelle saisie >> ")
            else:
                text = (Text("Le N° de contrat ne peut contenir de lettre ou vide", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau le N° du contrat souhaité :", style="red"))
                console.print(text)
                choice = Prompt.ask("Votre nouvelle saisie >> ")
