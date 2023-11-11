"""Module controller du menu Contrat"""
from controllers import menu_home_controller


class ContratController:
    """Menu controller pour l'ajout d'un Contrat à la BD Json"""

    def __init__(self):
        pass

    def add_contrat(self):
        print("ajout d'un Contrat")
        print("ajout d'un Contrat")
        print("ajout d'un Contrat")

    def modify_contrat(self):
        print("Modification d'un Contrat")
        print("Modification d'un Contrat")
        print("Modification d'un Contrat")

    def delete_contrat(self):
        print("Modification d'un Contrat")
        print("Modification d'un Contrat")
        print("Modification d'un Contrat")

    def view_all_contrat(self):
        print("Affichher tous les Contrat")
        print("Affichher tous les Contrat")
        print("Affichher tous les Contrat")

    def view_contrat(self):
        print("Afficher un Contrat")
        print("Afficher un Contrat")
        print("Afficher un Contrat")

    def menu_back(self):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_home_controller.HomeMenuController
        return self.handler
