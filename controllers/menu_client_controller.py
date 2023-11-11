"""Module controller du menu Client"""
from utils.menus import Menu
from controllers import menu_home_controller
from views.menu_client_view import ClientMenuView
from .client_controller import ClientController


class ClientMenuController:
    """menu controller pour les clients"""
    def __init__(self):
        self.menu = Menu()
        self.view = ClientMenuView(self.menu)

    def __call__(self):
        # 1. Construire le menu (utils/menus.py)
        self.menu.add("auto", "Afficher tous les clients", ClientController().view_all_client)
        self.menu.add("auto", "Afficher un client", ClientController().view_client)
        self.menu.add("auto", "Ajouter un client", ClientController().add_client)
        self.menu.add("auto", "Modifier un client", ClientController().delete_client)
        self.menu.add("auto", "Supprimer un client", ClientController().modify_client)
        # Ajouter les autres lignes d'option du menus
        self.menu.add("auto", "Menu principal", menu_home_controller.HomeMenuController())
        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()
        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler
