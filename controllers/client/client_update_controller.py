"""Module controller du Update menu client"""
from controllers.client import menu_update_client_controller
from models.client import Client
from models.employe import CustomUser
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from database import engine
from views.client.client_view import ClientView
from views.client.update_client_view import UpdateClientView
from utils.validate import Validate


class UpdateClientController:
    """Menu controller pour l'update du Client"""

    def __init__(self, token):
        self.client = Client
        self.user = CustomUser
        self.session = sessionmaker(bind=engine)
        self.view = ClientView()
        self.view_update = UpdateClientView
        self.token = token

    def list_client(self, token):
        """Module pour faire apparaitre la liste des clients"""
        session = self.session()
        clients = session.query(Client).all()
        session.close()
        self.view.view_clients(clients)
        choice = self.view_update.choice_user(self, clients)
        return choice

    def update_client_full_name(self, token):
        """Modification du nom et prénom du clients"""
        choice = UpdateClientController.list_client(self, self.token)
        new_full_name = self.view_update.update_full_name(self)
        # Sauvegarde du first_name dans la BD
        session = self.session()
        client = session.query(Client).filter_by(client_id=choice).first()
        client.full_name = new_full_name
        client.update_date = func.now()
        session.commit()
        session.close()
        validate = "La mise à jour du nom à été effectuée avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def update_client_email(self, token):
        """Modification de l'email du client"""
        choice = UpdateClientController.list_client(self, self.token)
        update_email = self.view_update.update_email(self)
        session = self.session()
        client = session.query(Client).filter_by(client_id=choice).first()
        client.email = update_email
        client.update_date = func.now()
        session.commit()
        session.close()
        validate = "La mise à jour de l'email à été effectuée avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def update_client_phone(self, token):
        """Modification du téléphone du client"""
        choice = UpdateClientController.list_client(self, self.token)
        update_phone = self.view_update.update_phone(self)
        session = self.session()
        client = session.query(Client).filter_by(client_id=choice).first()
        client.phone = update_phone
        client.update_date = func.now()
        session.commit()
        session.close()
        validate = "La mise à jour du téléphone à été effectuée avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def update_client_company_name(self, token):
        """Modification du nom de l'entreprise"""
        choice = UpdateClientController.list_client(self, self.token)
        update_company_name = self.view_update.update_company_name(self)
        session = self.session()
        client = session.query(Client).filter_by(client_id=choice).first()
        client.company_name = update_company_name
        client.update_date = func.now()
        session.commit()
        session.close()
        validate = "La mise à jour du nom de l'entreprise à été effectuée avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def update_client_commercial_id(self, token):
        """Modification du commercial de l'entreprise"""
        choice = UpdateClientController.list_client(self, self.token)
        session = self.session()
        client = session.query(Client).filter_by(client_id=choice).first()
        users = session.query(CustomUser).filter_by(role_id=1).all()
        self.view_update.view_commerciaux(self, users)
        choice_commercial = self.view_update.choice_commercial(self, users)
        client.commercial_id = choice_commercial
        client.update_date = func.now()
        session.commit()
        session.close()
        validate = "La mise à jour du commercial de l'entreprise à été effectuée avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def menu_back(self, token):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_update_client_controller.UpdateClientMenuController(token)
        return self.handler
