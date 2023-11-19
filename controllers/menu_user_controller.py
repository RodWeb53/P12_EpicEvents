"""Module controller du menu Client"""
from utils.menus import Menu
from utils.clean_screen import clear
from controllers import menu_home_controller
from views.menu_user_view import UserMenuView
from .user_controller import UserController
from .menu_update_user_controller import UpdateUserMenuController
from controllers.auth_controller import AuthController


class UserMenuController:
    """menu controller pour les clients"""
    def __init__(self, token):
        self.menu = Menu()
        self.view = UserMenuView(self.menu)
        self.token = token

    def __call__(self, token):
        clear()
        # 1. Construire le menu (utils/menus.py)
        auth = AuthController.decrypt_token(self, self.token)
        self.menu.add("auto", "Afficher tous les utilisateurs", UserController(self.token).view_all_user)
        self.menu.add("auto", "Afficher un utilisateur", UserController(self.token).view_user)
        # Vérification des droits via la token
        if auth["role_id"] == 2:
            self.menu.add("auto", "Ajouter un utilisateur", UserController(self.token).add_user)
            self.menu.add("auto", "Modifier un utilisateur", UpdateUserMenuController(self.token))
            self.menu.add("auto", "Supprimer un utilisateur", UserController(self.token).delete_user)

        # Ajout de la ligne de retour au menu
        self.menu.add("auto", "Menu principal", menu_home_controller.HomeMenuController())
        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur

        user_choice = self.view.get_user_choice()
        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler
