from utils.client import UtilsClient
from controllers.auth_controller import AuthController


class ClientView:

    def __init__(self):
        self.utils_client = UtilsClient

    def new_client(self, token):
        auth = AuthController.decrypt_token(self, token)
        new_client_add = {}
        create_entry = True
        while create_entry:
            client_last_name = self.utils_client.display_menu_last_name(self)
            client_first_name = self.utils_client.display_menu_first_name(self)
            full_name = f"{client_last_name} - {client_first_name}"
            email = self.utils_client.display_menu_email(self)
            phone = self.utils_client.display_menu_phone(self)
            company_name = self.utils_client.display_menu_company_name(self)
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
