"""Module controller du menu Evenement"""
from controllers import menu_home_controller


class EventController:
    """Menu controller pour l'ajout d'un Evenement à la BD Json"""

    def __init__(self):
        pass

    def add_event(self):
        print("ajout d'un Evenement")
        print("ajout d'un Evenement")
        print("ajout d'un Evenement")

    def modify_event(self):
        print("Modification d'un Evenement")
        print("Modification d'un Evenement")
        print("Modification d'un Evenement")

    def delete_event(self):
        print("Modification d'un Evenement")
        print("Modification d'un Evenement")
        print("Modification d'un Evenement")

    def view_all_event(self):
        print("Affichher tous les Evenements")
        print("Affichher tous les Evenements")
        print("Affichher tous les Evenements")

    def view_event(self):
        print("Afficher un Evenement")
        print("Afficher un Evenement")
        print("Afficher un Evenement")

    def view_unassociated_event(self):
        print("Afficher les Evenements non associés")
        print("Afficher les Evenements non associés")
        print("Afficher les Evenements non associés")

    def view_associated_event(self):
        print("Associer un support à un événement")
        print("Associer un support à un événement")
        print("Associer un support à un événement")

    def view_my_events(self):
        print("Afficher mes Evenements")
        print("Afficher mes Evenements")
        print("Afficher mes Evenements")

    def menu_back(self):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_home_controller.HomeMenuController
        return self.handler
