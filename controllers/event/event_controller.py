"""Module controller du menu Evenement"""
from controllers import menu_home_controller
from views.event.event_view import EventView
from models.event import Event
from models.contract import Contract
from models.employe import CustomUser
from sqlalchemy.orm import sessionmaker
from database import engine
from utils.validate import Validate


class EventController:
    """Menu controller pour l'ajout d'un Evenement à la BD Json"""

    def __init__(self, token):
        self.session = sessionmaker(bind=engine)
        self.view = EventView()
        self.token = token
        self.event = Event

    def add_event(self, token):
        session = self.session()
        contracts = session.query(Contract).all()
        supports = session.query(CustomUser).filter_by(role_id=2).all()
        session.close()
        add_event = self.view.add_event(self.token, contracts, supports)
        if not add_event == -1:
            contract = self.event(**add_event)
            session.add(contract)
            session.commit()
            session.close()
            validate = "L'événement à été créé avec succès dans la bd"
            Validate.validate_bd(self, validate)
            return self.menu_back(self.token)
        else:
            validate = "L'événement ne sera pas enregistré"
            Validate.validate_bd(self, validate)
            return self.menu_back(self.token)

    def modify_event(self, token):
        print("Modification d'un Evenement")
        print("Modification d'un Evenement")
        print("Modification d'un Evenement")

    def delete_event(self, token):
        print("Modification d'un Evenement")
        print("Modification d'un Evenement")
        print("Modification d'un Evenement")

    def view_all_event(self, token):
        print("Affichher tous les Evenements")
        print("Affichher tous les Evenements")
        print("Affichher tous les Evenements")

    def view_event(self, token):
        print("Afficher un Evenement")
        print("Afficher un Evenement")
        print("Afficher un Evenement")

    def view_unassociated_event(self, token):
        print("Afficher les Evenements non associés")
        print("Afficher les Evenements non associés")
        print("Afficher les Evenements non associés")

    def view_associated_event(self, token):
        print("Associer un support à un événement")
        print("Associer un support à un événement")
        print("Associer un support à un événement")

    def view_my_events(self, token):
        print("Afficher mes Evenements")
        print("Afficher mes Evenements")
        print("Afficher mes Evenements")

    def menu_back(self, token):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_home_controller.HomeMenuController()
        return self.handler
