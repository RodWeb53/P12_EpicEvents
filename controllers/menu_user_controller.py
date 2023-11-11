"""Module controller du menu Client"""
from utils.menus import Menu
from controllers import menu_home_controller
from views.menu_user_view import UserMenuView
from .user_controller import UserController


class UserMenuController:
    """menu controller pour les clients"""
    def __init__(self):
        self.menu = Menu()
        self.view = UserMenuView(self.menu)

    def __call__(self):
        # 1. Construire le menu (utils/menus.py)
        self.menu.add("auto", "Afficher tous les utilistaeurs", UserController().view_all_user)
        self.menu.add("auto", "Afficher un utilisateur", UserController().view_user)
        self.menu.add("auto", "Ajouter un utilisateur", UserController().add_user)
        self.menu.add("auto", "Modifier un utilisateur", UserController().delete_user)
        self.menu.add("auto", "Supprimer un utilisateur", UserController().modify_user)
        # Ajouter les autres lignes d'option du menus
        self.menu.add("auto", "Menu principal", menu_home_controller.HomeMenuController())
        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()
        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler
