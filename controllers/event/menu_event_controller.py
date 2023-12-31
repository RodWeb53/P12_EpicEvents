"""Module controller du menu Evenement"""
from utils.menus import Menu
from controllers import menu_home_controller
from views.event.menu_event_view import EventMenuView
from .event_controller import EventController


class EventMenuController:
    """menu controller pour les contrats"""
    def __init__(self, token):
        self.menu = Menu()
        self.view = EventMenuView(self.menu)
        self.token = token

    def __call__(self, token):
        # 1. Construire le menu (utils/menus.py)
        self.menu.add("auto", "Afficher tous les événements", EventController(self.token).view_all_event)
        self.menu.add("auto", "Afficher un événement", EventController(self.token).view_event)
        self.menu.add("auto", "Ajouter un événement", EventController(self.token).add_event)
        self.menu.add("auto", "Afficher les événements non associés", EventController(self.token).view_unassociated_event)
        self.menu.add("auto", "Associer un support à un événement", EventController(self.token).view_associated_event)
        self.menu.add("auto", "Afficher mes événements", EventController(self.token).view_my_events)
        self.menu.add("auto", "Modifier un événement", EventController(self.token).delete_event)
        self.menu.add("auto", "Supprimer un événement", EventController(self.token).modify_event)
        # Ajouter les autres lignes d'option du menus
        self.menu.add("auto", "Menu principal", menu_home_controller.HomeMenuController())
        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()
        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler
