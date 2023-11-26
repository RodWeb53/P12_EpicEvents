"""Module controller du menu Contrat"""
from controllers import menu_home_controller
from views.contract_view import ContractView
from sqlalchemy.orm import sessionmaker
from database import engine
from models.client import Client
from models.contract import Contract
from rich.console import Console
from rich.text import Text


class ContratController:
    """Menu controller pour l'ajout d'un Contrat à la BD Json"""

    def __init__(self, token):
        self.session = sessionmaker(bind=engine)
        self.token = token
        self.contract = Contract
        self.view = ContractView()

    def add_contrat(self, token):
        console = Console()
        session = self.session()
        clients = session.query(Client).all()
        session.close()
        add_contract = self.view.add_contract(self.token, clients)
        session = self.session()
        if not add_contract == -1:
            contract = self.contract(**add_contract)
            session.add(contract)
            session.commit()
            text = (Text("Le contrat à été créé avec succès dans la bd", style="green"))
            console.print(text)
            session.close()
            text = (Text("Appuyer sur entrée pour revenir au menu", style="red"))
            console.print(text)
            input("")
            return self.menu_back(self.token)
        else:
            text = (Text("le contrat ne sera pas enregistré", style="red"))
            console.print(text)
            text = (Text("Appuyer sur entrée pour revenir au menu", style="red"))
            console.print(text)
            input("")
            return self.menu_back(self.token)

    def modify_contrat(self, token):
        print("Modification d'un Contrat")
        print("Modification d'un Contrat")
        print("Modification d'un Contrat")

    def delete_contrat(self, token):
        print("Modification d'un Contrat")
        print("Modification d'un Contrat")
        print("Modification d'un Contrat")

    def view_all_contrat(self, token):
        print("Affichher tous les Contrat")
        print("Affichher tous les Contrat")
        print("Affichher tous les Contrat")

    def view_contrat(self, token):
        print("Afficher un Contrat")
        print("Afficher un Contrat")
        print("Afficher un Contrat")

    def menu_back(self, token):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_home_controller.HomeMenuController()
        return self.handler
