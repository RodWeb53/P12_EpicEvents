"""Module controller du menu Client"""
from controllers import menu_home_controller
from models.client import Client
from views.client_view import ClientView
from sqlalchemy.orm import sessionmaker
from database import engine
from rich.console import Console
from rich.text import Text


class ClientController:
    """Menu controller pour l'ajout d'un Client à la BD Json"""

    def __init__(self, token):
        self.session = sessionmaker(bind=engine)
        self.client = Client
        self.view = ClientView()
        self.token = token

    def add_client(self, token):
        new_client = self.view.new_client(self.token)
        console = Console()
        session = self.session()
        if not new_client == -1:
            client = self.client(**new_client)
            session.add(client)
            session.commit()
            text = (Text("Le client à été créé avec succès dans la bd", style="green"))
            console.print(text)
            session.close()
            text = (Text("Appuyer sur entrée pour revenir au menu", style="red"))
            console.print(text)
            input("")
            return self.menu_back(self.token)
        else:
            text = (Text("l'utilisateur ne sera pas enregistré", style="red"))
            console.print(text)
            text = (Text("Appuyer sur entrée pour revenir au menu", style="red"))
            console.print(text)
            input("")
            return self.menu_back()

    def modify_client(self):
        print("Modification d'un client")
        print("Modification d'un client")
        print("Modification d'un client")

    def delete_client(self):
        print("Suppression d'un client")
        print("Suppression d'un client")
        print("Suppression d'un client")

    def view_all_client(self, token):
        print("Afficher tous les clients")
        print("Afficher tous les clients")
        print("Afficher tous les clients")

    def view_client(self):
        print("Afficher un client")
        print("Afficher un client")
        print("Afficher un client")

    def menu_back(self, token):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_home_controller.HomeMenuController()
        return self.handler
