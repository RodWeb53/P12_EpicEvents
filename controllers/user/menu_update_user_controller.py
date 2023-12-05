"""Module controller du menu USER"""
from utils.menus import Menu
from utils.clean_screen import clear
from controllers import menu_home_controller
from views.user.menu_update_user import UpdateUserMenuView
from .user_update_controller import UpdateUserController
from controllers.auth_controller import AuthController


class UpdateUserMenuController:
    """menu controller pour les Users"""
    def __init__(self, token):
        self.menu = Menu()
        self.view = UpdateUserMenuView(self.menu)
        self.token = token

    def __call__(self, token):
        clear()
        # 1. Construire le menu (utils/menus.py)
        auth = AuthController.decrypt_token(self, self.token)
        if auth["role_id"] == 2:
            self.menu.add("auto", "Modification du nom", UpdateUserController(self.token).update_user_last_name)
            self.menu.add("auto", "Modification du prénom", UpdateUserController(self.token).update_user_first_name)
            self.menu.add("auto", "Modification de l'email", UpdateUserController(self.token).update_user_email)
            self.menu.add("auto", "Modification du Tel fixe", UpdateUserController(self.token).update_user_phone)
            self.menu.add("auto", "Modification du Tel mobile", UpdateUserController(self.token).update_user_phone_mobile)
            self.menu.add("auto", "Modification du role", UpdateUserController(self.token).update_user_role)
            self.menu.add("auto", "Modification utilisateur actif", UpdateUserController(self.token).update_user_is_active)

        # Ajout de la ligne de retour au menu
        self.menu.add("auto", "Menu principal", menu_home_controller.HomeMenuController())
        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur

        user_choice = self.view.get_user_choice()
        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler
