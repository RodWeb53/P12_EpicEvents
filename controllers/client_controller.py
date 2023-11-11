"""Module controller du menu Client"""
from controllers import menu_home_controller


class ClientController:
    """Menu controller pour l'ajout d'un Client à la BD Json"""

    def __init__(self):
        pass

    def add_client(self):
        print("ajout d'un client")
        print("ajout d'un client")
        print("ajout d'un client")

    def modify_client(self):
        print("Modification d'un client")
        print("Modification d'un client")
        print("Modification d'un client")

    def delete_client(self):
        print("Suppression d'un client")
        print("Suppression d'un client")
        print("Suppression d'un client")

    def view_all_client(self):
        print("Afficher tous les clients")
        print("Afficher tous les clients")
        print("Afficher tous les clients")

    def view_client(self):
        print("Afficher un client")
        print("Afficher un client")
        print("Afficher un client")

    def menu_back(self):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_home_controller.HomeMenuController
        return self.handler
