"""Module controller du menu contrat"""
from utils.menus import Menu
from utils.clean_screen import clear
from controllers import menu_home_controller
from views.contract.menu_update_contrat_view import UpdateContractMenuView
from .contrat_update_controller import UpdateContractController
from controllers.auth_controller import AuthController


class UpdateContratMenuController:
    """menu controller pour les clients"""
    def __init__(self, token):
        self.menu = Menu()
        self.view = UpdateContractMenuView(self.menu)
        self.token = token

    def __call__(self, token):
        clear()
        # 1. Construire le menu (utils/menus.py)
        auth = AuthController.decrypt_token(self, self.token)
        if auth["role_id"] == 2:
            self.menu.add("auto", "Modification du montant du contrat",
                          UpdateContractController(self.token).update_contract_amount)
            self.menu.add("auto", "Modification du montant restant à recevoir",
                          UpdateContractController(self.token).update_due_payment)
            self.menu.add("auto", "Modification du statut du contrat",
                          UpdateContractController(self.token).update_contract_status)

        # Ajout de la ligne de retour au menu
        self.menu.add("auto", "Menu principal", menu_home_controller.HomeMenuController())
        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur

        user_choice = self.view.get_user_choice()
        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler
