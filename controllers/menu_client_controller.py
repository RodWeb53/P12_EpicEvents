"""Module controller du menu Client"""
from utils.menus import Menu
from controllers import menu_home_controller
from views.menu_client_view import ClientMenuView
from .client_controller import ClientController
from .menu_update_client_controller import UpdateClientMenuController
from controllers.auth_controller import AuthController


class ClientMenuController:
    """menu controller pour les clients"""
    def __init__(self, token):
        self.menu = Menu()
        self.view = ClientMenuView(self.menu)
        self.token = token

    def __call__(self, token):
        # 1. Construire le menu (utils/menus.py)
        auth = AuthController.decrypt_token(self, self.token)
        print(auth)
        self.menu.add("auto", "Afficher tous les clients", ClientController(self.token).view_all_client)
        self.menu.add("auto", "Afficher un client", ClientController(self.token).view_client)
        self.menu.add("auto", "Ajouter un client", ClientController(self.token).add_client)
        self.menu.add("auto", "Modifier un client", UpdateClientMenuController(self.token))
        self.menu.add("auto", "Supprimer un client", ClientController(self.token).modify_client)
        # Ajouter les autres lignes d'option du menus
        self.menu.add("auto", "Menu principal", menu_home_controller.HomeMenuController())
        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()
        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler
