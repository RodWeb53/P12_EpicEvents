"""Module controller du menu Contrat"""
from controllers import menu_home_controller
from controllers.contract.contrat_update_controller import UpdateContractController
from views.contract.contract_view import ContractView
from views.contract.update_contrat_view import UpdateContractView
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.sql import func
from database import engine
from models.client import Client
from models.contract import Contract
from utils.validate import Validate


class ContratController:
    """Menu controller pour l'ajout d'un Contrat à la BD Json"""

    def __init__(self, token):
        self.session = sessionmaker(bind=engine)
        self.token = token
        self.contract = Contract
        self.view = ContractView()
        self.view_update = UpdateContractView

    def add_contrat(self, token):
        session = self.session()
        clients = session.query(Client).all()
        session.close()
        add_contract = self.view.add_contract(self.token, clients)
        session = self.session()
        if not add_contract == -1:
            contract = self.contract(**add_contract)
            session.add(contract)
            session.commit()
            session.close()
            validate = "Le contrat à été créé avec succès dans la bd"
            Validate.validate_bd(self, validate)
            return self.menu_back(self.token)
        else:
            validate = "le contrat ne sera pas enregistré"
            Validate.validate_bd(self, validate)
            return self.menu_back(self.token)

    def delete_contrat(self, token):
        choice = UpdateContractController.list_contract(self, self.token)
        session = self.session()
        contract = session.query(Contract).filter_by(contract_id=choice).first()
        session.delete(contract)
        session.commit()
        session.close()
        validate = "La suppression du contrat à été effectuée avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def view_unsigned_contract(self, token):
        session = self.session()
        contracts = session.query(Contract).filter_by(contract_status=False).all()
        session.close()
        self.view.view_contracts(contracts)
        validate = ""
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def view_unsettled_contract(self, token):
        session = self.session()
        contracts = session.query(Contract).filter(Contract.due_payment < Contract.contract_amount).all()
        session.close()
        self.view.view_contracts(contracts)
        validate = ""
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def list_all_contract(self, token):
        """List de tous les contrats"""
        session = self.session()
        contracts = session.query(Contract).all()
        session.close()
        return contracts

    def view_all_contrat(self, token):
        contracts = ContratController.list_all_contract(self, token)
        self.view.view_contracts(contracts)
        validate = ""
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def view_contrat(self, token):
        contracts = ContratController.list_all_contract(self, token)
        self.view.view_contracts(contracts)
        choice = self.view.choice_user(contracts)
        session = self.session()
        contract = session.query(Contract).filter_by(contract_id=int(choice)).first()
        session.close()
        self.view.view_one_contract(contract)
        validate = ""
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def menu_back(self, token):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_home_controller.HomeMenuController()
        return self.handler
