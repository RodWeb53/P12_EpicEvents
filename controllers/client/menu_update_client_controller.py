"""Module controller du menu Client"""
from utils.menus import Menu
from utils.clean_screen import clear
from controllers import menu_home_controller
from views.client.menu_update_client import UpdateClientMenuView
from .client_update_controller import UpdateClientController
from controllers.auth_controller import AuthController


class UpdateClientMenuController:
    """menu controller pour les clients"""
    def __init__(self, token):
        self.menu = Menu()
        self.view = UpdateClientMenuView(self.menu)
        self.token = token

    def __call__(self, token):
        clear()
        # 1. Construire le menu (utils/menus.py)
        auth = AuthController.decrypt_token(self, self.token)
        if auth["role_id"] == 2:
            self.menu.add("auto", "Modification du nom complet",
                          UpdateClientController(self.token).update_client_full_name)
            self.menu.add("auto", "Modification de l'email",
                          UpdateClientController(self.token).update_client_email)
            self.menu.add("auto", "Modification du Téléphone",
                          UpdateClientController(self.token).update_client_phone)
            self.menu.add("auto", "Modification du nom de l'entreprise",
                          UpdateClientController(self.token).update_client_company_name)
            self.menu.add("auto", "Modification contact commercial",
                          UpdateClientController(self.token).update_client_commercial_id)

        # Ajout de la ligne de retour au menu
        self.menu.add("auto", "Menu principal", menu_home_controller.HomeMenuController())
        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur

        user_choice = self.view.get_user_choice()
        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler
