"""Module controller du menu Client"""
from controllers.client import menu_client_controller
from models.client import Client
from views.client.client_view import ClientView
from utils.validate import Validate
from sqlalchemy.orm import sessionmaker
from database import engine


class ClientController:
    """Menu controller pour l'ajout d'un Client à la BD Json"""

    def __init__(self, token):
        self.session = sessionmaker(bind=engine)
        self.client = Client
        self.view = ClientView()
        self.token = token

    def add_client(self, token):
        new_client = self.view.new_client(self.token)
        session = self.session()
        if not new_client == -1:
            client = self.client(**new_client)
            session.add(client)
            session.commit()
            validate = "Le client à été créé avec succès dans la bd"
            Validate.validate_bd(self, validate)
            return self.menu_back(self.token)
        else:
            validate = "l'utilisateur ne sera pas enregistré"
            Validate.validate_bd(self, validate)
            return self.menu_back()

    def delete_client(self):
        print("Suppression d'un client")
        print("Suppression d'un client")
        print("Suppression d'un client")

    def view_all_client(self, token):
        session = self.session()
        clients = session.query(Client).all()
        session.close()
        self.view.view_clients(clients)
        validate = ""
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def view_client(self, token):
        session = self.session()
        clients = session.query(Client).all()
        session.close()
        self.view.view_clients(clients)
        choice = self.view.choice_user(clients)
        session = self.session()
        client = session.query(Client).filter_by(client_id=int(choice)).first()
        self.view.view_one_client(client)
        validate = ""
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def menu_back(self, token):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_client_controller.ClientMenuController(token)
        return self.handler
