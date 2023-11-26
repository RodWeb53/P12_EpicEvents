from rich.prompt import Prompt
from rich.console import Console
from rich.text import Text


class UtilsContract:

    def __init__(self):
        pass

    def display_contract_amount(self):
        """Demande du montant du contrat"""
        console = Console()
        print("")
        text = (Text("Entrez le montant du contrat :", style="blue"))
        console.print(text)
        contract_amount = Prompt.ask("Votre saisie >> ")
        create_entry = True
        while create_entry:
            try:
                float(contract_amount)
                create_entry = False
                return contract_amount
            except ValueError:
                text = (Text("Le montant est obligatoirement en chiffre", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau un montant :", style="red"))
                console.print(text)
                contract_amount = Prompt.ask("Votre nouvelle saisie >> ")

    def display_contract_due_payment(self):
        """Demande des sommes reçues"""
        console = Console()
        print("")
        text = (Text("Entrez le montant reçue :", style="blue"))
        console.print(text)
        contract_amount = Prompt.ask("Votre saisie >> ")
        create_entry = True
        while create_entry:
            try:
                float(contract_amount)
                create_entry = False
                return contract_amount
            except ValueError:
                text = (Text("Le montant est obligatoirement en chiffre", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau un montant :", style="red"))
                console.print(text)
                contract_amount = Prompt.ask("Votre nouvelle saisie >> ")

    def display_menu_status_contract(self):
        """Demande sur le status du contrat (signé ou pas)"""
        console = Console()
        print("")
        text = (Text("Le contrat est il signé ? :", style="blue"))
        console.print(text)
        text = (Text("   o  /  n \n", style="red"))
        console.print(text)
        staus_contract = Prompt.ask("Votre saisie >> ")
        verify = True
        while verify:
            if staus_contract.lower() == "o":
                verify = False
                return True
            elif staus_contract.lower() == "n":
                verify = False
                return False
            else:
                text = (Text("La réponse saisie n'est pas correcte", style="red"))
                console.print(text)
                text = (Text("   o  /  n \n", style="red"))
                console.print(text)
                staus_contract = Prompt.ask("Votre nouvelle saisie >> ")

    def display_menu_choice_client(self, clients):
        """Demande le numéro du client à associer au contrat"""
        list_clients = []
        console = Console()
        print("")
        text = (Text("Entrez le code du client :", style="blue"))
        console.print(text)
        client_id = Prompt.ask("Votre saisie >> ")
        for client in clients:
            list_clients.append(client.client_id)
        create_entry = True

        while create_entry:
            if client_id.isnumeric():
                if int(client_id) in list_clients:
                    create_entry = False
                    return client_id
                else:
                    text = (Text("Le numéro du client saisie n'est pas connue dans la base de données ", style="red"))
                    console.print(text)
                    text = (Text("Entrez de nouveau un numéro :", style="red"))
                    console.print(text)
                    client_id = Prompt.ask("Votre nouvelle saisie >> ")
            else:
                text = (Text("Le numéro du client saisie n'est pas un chiffre ", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau un numéro :", style="red"))
                console.print(text)
                client_id = Prompt.ask("Votre nouvelle saisie >> ")

    def display_menu_contract_choice_save(self):
        """Vérification si l'utilisateur veut enregistrer le nouveau contrat'"""
        console = Console()
        verify = True
        while verify:
            print("")
            text = (Text("Confirmez la création du nouveau contrat : \n", style="blue"))
            console.print(text)
            text = (Text("   o / n \n", style="red"))
            console.print(text)
            user_choice_save = input("Votre confirmation >>  ")
            if user_choice_save == "o" or user_choice_save == "n":
                verify = False

        return user_choice_save
