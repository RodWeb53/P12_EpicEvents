from utils.contract import UtilsContract


class ContractView:

    def __init__(self):
        self.utils = UtilsContract

    def add_contract(self, token, clients):
        print("dans la vue de contrat")
        new_contract_add = {}
        create_entry = True
        while create_entry:
            contract_amount = self.utils.display_contract_amount(self)
            due_payment = self.utils.display_contract_due_payment(self)
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
