""" Module controller"""
from .menu_home_controller import HomeMenuController


class ApplicationController:
    """Home menu controller"""
    def __init__(self):
        self.controller = None

    def start(self):
        """Fonction de démarrage de l'application"""
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()
