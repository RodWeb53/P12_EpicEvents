"""Module controller du menu Utilisateur"""
from controllers import menu_user_controller
from models.employe import CustomUser
from utils.user import UtilsUser
from utils.validate import Validate
from views.user_view import AddUserView, EditUserView
from sqlalchemy.orm import sessionmaker
from database import engine


class UserController:
    """Menu controller pour l'ajout d'un Utilisateur à la BD"""

    def __init__(self, token):
        self.session = sessionmaker(bind=engine)
        self.user = CustomUser
        self.view = AddUserView()
        self.token = token

    def add_user(self, token):
        """ Création d'un employé """
        user_create = self.view.new_user()
        session = self.session()
        if not user_create == -1:
            user = self.user(**user_create)
            session.add(user)
            session.commit()
            session.close()
            validate = "L'employé à été créé avec succès dans la bd"
            Validate.validate_bd(self, validate)
            return self.menu_back(self.token)
        else:
            validate = "l'utilisateur ne sera pas enregistré"
            Validate.validate_bd(self, validate)
            return self.menu_back()

    def delete_user(self, token):
        """Suppression dans la BD de l'employé"""
        verify = True
        while verify:
            # Demande du N° d'utilisateur à supprimer
            choice = UtilsUser.display_menu_user_choice_modify(self)
            # vérification que l'utilisateur est connue
            session = self.session()
            user = session.query(CustomUser).filter_by(id=choice).first()
            session.close()
            if user is not None:
                verify = False

        # Suppression de l'employé dans la BD
        session = self.session()
        user = session.query(CustomUser).filter_by(id=choice).first()
        session.delete(user)
        session.commit()
        session.close()
        validate = "L'employé à été supprimé avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def view_all_user(self, token):
        session = self.session()
        users = session.query(CustomUser).all()
        session.close()
        EditUserView.view_users(self, users)
        validate = ""
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def view_user(self, token):
        choice = EditUserView.choice_user(self)
        session = self.session()
        user = session.query(CustomUser).filter_by(id=choice).first()
        session.close()
        EditUserView.view_one_user(self, user)
        validate = ""
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def menu_back(self, token):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_user_controller.UserMenuController(token)
        return self.handler
