"""Module controller du menu d'accueil"""
from utils.menus import Menu
from utils.clean_screen import clear
from views.menu_home_view import HomeMenuView
from .menu_client_controller import ClientMenuController
from .menu_contrat_controller import ContratMenuController
from .menu_event_controller import EventMenuController
from .menu_user_controller import UserMenuController


class HomeMenuController():
    """Home Menu controller"""
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, token):
        clear()
        # 1. Construire le menu (utils/menus.py)
        self.menu.add("auto", "Gestion des clients", ClientMenuController(token))
        self.menu.add("auto", "Gestion des contrats", ContratMenuController(token))
        self.menu.add("auto", "Gestion des événements", EventMenuController(token))
        self.menu.add("auto", "Gestion des utilisateurs", UserMenuController(token))
        self.menu.add("q", "Quitter l'application", self.end_screen_controller())
        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()
        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler

    def end_screen_controller(self):
        """Sortie du programme"""
        return
