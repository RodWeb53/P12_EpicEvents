"""Module controller du menu Utilisateur"""
from controllers import menu_user_controller
# from utils.user import UtilsUser
from models.employe import CustomUser
from views.user_view import AddUserView, EditUserView
from sqlalchemy.orm import sessionmaker
from database import engine
from rich.console import Console
from rich.text import Text


class UserController:
    """Menu controller pour l'ajout d'un Utilisateur à la BD"""

    def __init__(self, token):
        self.session = sessionmaker(bind=engine)
        self.user = CustomUser
        self.view = AddUserView()
        self.token = token

    def add_user(self, token):
        """ Création d'un employé """
        console = Console()
        user_create = self.view.new_user()
        session = self.session()
        if not user_create == -1:
            user = self.user(**user_create)
            session.add(user)
            session.commit()
            text = (Text("L'employé à été créé avec succès dans la bd", style="green"))
            console.print(text)
            session.close()
            text = (Text("Appuyer sur entrée pour revenir au menu", style="red"))
            console.print(text)
            input("")
            return self.menu_back(self.token)
        else:
            text = (Text("l'utilisateur ne sera pas enregistré", style="red"))
            console.print(text)
            return self.menu_back()

    def modify_user(self, token):
        print("Modification d'un utilisateur")
        print("Modification d'un utilisateur")
        print("Modification d'un utilisateur")

    def delete_user(self):
        print("Suppression d'un utilisateur")
        print("Suppression d'un utilisateur")
        print("Suppression d'un utilisateur")

    def view_all_user(self, token):
        console = Console()
        session = self.session()
        users = session.query(CustomUser).all()
        session.close()
        EditUserView.view_users(self, users)
        text = (Text("Appuyer sur entrée pour revenir au menu", style="red"))
        console.print(text)
        input("")
        return self.menu_back(self.token)

    def view_user(self, token):
        choice = EditUserView.choice_user(self)
        session = self.session()
        user = session.query(CustomUser).filter_by(id=choice).first()
        session.close()
        EditUserView.view_one_user(self, user)
        text = (Text("Appuyer sur entrée pour revenir au menu", style="red"))
        console = Console()
        console.print(text)
        input("")
        return self.menu_back(self.token)

    def menu_back(self, token):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_user_controller.UserMenuController(token)
        return self.handler
