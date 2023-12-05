"""Module controller du menu Contrat"""
from utils.menus import Menu
from controllers import menu_home_controller
from views.contract.menu_contrat_view import ContratMenuView
from .menu_update_contrat_controller import UpdateContratMenuController
from .contrat_controller import ContratController


class ContratMenuController:
    """menu controller pour les contrats"""
    def __init__(self, token):
        self.menu = Menu()
        self.view = ContratMenuView(self.menu)
        self.token = token

    def __call__(self, token):
        # 1. Construire le menu (utils/menus.py)
        self.menu.add("auto", "Afficher tous les contrats", ContratController(self.token).view_all_contrat)
        self.menu.add("auto", "Afficher un contrat", ContratController(self.token).view_contrat)
        self.menu.add("auto", "Ajouter un contrat", ContratController(self.token).add_contrat)
        self.menu.add("auto", "Modifier un contrat", UpdateContratMenuController(self.token))
        self.menu.add("auto", "Afficher les contrats non signés", ContratController(self.token).view_unsigned_contract)
        self.menu.add("auto", "Afficher les contrats non payés", ContratController(self.token).view_unsettled_contract)
        self.menu.add("auto", "Supprimer un contrat", ContratController(self.token).delete_contrat)
        # Ajouter les autres lignes d'option du menus
        self.menu.add("auto", "Menu principal", menu_home_controller.HomeMenuController())
        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()
        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler
