from utils.contract import UtilsContract
from rich.console import Console
# from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
# from utils.clean_screen import clear


class UpdateContractView:

    def __init__(self):
        self.utils_contract = UtilsContract

    def update_contract_amount(self):
        """Modification du montant du contrat"""
        change = "modifié du contrat"
        update_contract_amount = UtilsContract.display_contract_amount(self, change)
        return update_contract_amount

    def update_due_payment(self):
        """Modification des sommes versés"""
        change = "du contrat modifié"
        update_due_payment = UtilsContract.display_contract_due_payment(self, change)
        return update_due_payment

    def update_contract_status(self):
        """Modification du status du contrat"""
        contract_status = UtilsContract.display_menu_status_contract(self)
        return contract_status

    def choice_user(self, contracts):
        """Module pour connaitre le contrat à modifier et vérifier s'il est dans la liste"""
        console = Console()
        list_contracts = []
        text = (Text("Entrez le N° de contrat que vous souhaitez modifier :", style="blue"))
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
                    text = (Text("Le numéro du contrat saisie n'est pas connue dans la base de données ", style="red"))
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
