"""Module controller du update menu contrat"""
from controllers.contract import menu_update_contrat_controller
from models.contract import Contract
from models.employe import CustomUser
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from database import engine
from views.contract.contract_view import ContractView
from views.contract.update_contrat_view import UpdateContractView
from utils.validate import Validate


class UpdateContractController:
    """Menu controller pour l'update du contrat"""

    def __init__(self, token):
        self.user = CustomUser
        self.contract = Contract
        self.view = ContractView()
        self.view_update = UpdateContractView
        self.session = sessionmaker(bind=engine)
        self.token = token

    def list_contract(self, token):
        """Module pour faire apparaitre la liste des contratt"""
        session = self.session()
        contracts = session.query(Contract).all()
        session.close()
        self.view.view_contracts(contracts)
        choice = self.view_update.choice_user(self, contracts)
        return choice

    def update_contract_amount(self, token):
        """Modification du montant du contrat"""
        choice = UpdateContractController.list_contract(self, self.token)
        new_contract_amount = self.view_update.update_contract_amount(self)
        session = self.session()
        contract = session.query(Contract).filter_by(contract_id=choice).first()
        contract.contract_amount = new_contract_amount
        contract.update_date = func.now()
        session.commit()
        session.close()
        validate = "La mise à jour du montant du contrat à été effectuée avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def update_due_payment(self, token):
        """Modification du montant restant à recevoir"""
        choice = UpdateContractController.list_contract(self, self.token)
        new_due_payment = self.view_update.update_due_payment(self)
        session = self.session()
        contract = session.query(Contract).filter_by(contract_id=choice).first()
        contract.due_payment = float(contract.due_payment) + float(new_due_payment)
        contract.update_date = func.now()
        session.commit()
        session.close()
        validate = "La mise à jour du montant du contrat à été effectuée avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def update_contract_status(self, token):
        """Modification du status du contrat"""
        choice = UpdateContractController.list_contract(self, self.token)
        new_contract_status = self.view_update.update_contract_status(self)
        session = self.session()
        contract = session.query(Contract).filter_by(contract_id=choice).first()
        contract.contract_status = new_contract_status
        contract.update_date = func.now()
        session.commit()
        session.close()
        validate = "La mise à jour du montant du contrat à été effectuée avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def menu_back(self, token):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_update_contrat_controller.UpdateContratMenuController(token)
        return self.handler
