"""Module controller du menu Utilisateur"""
from controllers import menu_home_controller
from models.employe import CustomUser
from views.user_view import AddUserView
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
        else:
            text = (Text("l'utilisateur ne sera pas enregistré", style="red"))
            console.print(text)
            return self.menu_back()

    def modify_user(self):
        print("Modification d'un utilisateur")
        print("Modification d'un utilisateur")
        print("Modification d'un utilisateur")

    def delete_user(self):
        print("Suppression d'un utilisateur")
        print("Suppression d'un utilisateur")
        print("Suppression d'un utilisateur")

    def view_all_user(self):
        print("Afficher tous les utilisateurs")
        print("Afficher tous les utilisateurs")
        print("Afficher tous les utilisateurs")

    def view_user(self):
        print("Afficher un utilisateur")
        print("Afficher un utilisateur")
        print("Afficher un utilisateur")

    def menu_back(self):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_home_controller.HomeMenuController
        return self.handler
