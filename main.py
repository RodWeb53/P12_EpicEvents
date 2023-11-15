"""Module main pour lancer l'application"""
from controllers.application_controller import ApplicationController
from controllers.auth_controller import AuthController
from models.employe import CustomUser
from database import engine
from sqlalchemy.orm import sessionmaker
from views.auth_view import AuthView
from rich import print
from rich.console import Group
from rich.panel import Panel
from utils.clean_screen import clear

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    user = CustomUser
    session = Session()
    users = session.query(CustomUser).all()
    session.close()
    self = ""
    clear()

    panel_group = Group(
        Panel("Bienvenue chez Epic Events", width=80, style="blue"),
        Panel("Connexion", width=80, style="blue")
    )
    print(Panel(panel_group, width=80, style="blue"))
    login = AuthView.verify_login(self, users)

    password = AuthView.verify_password(self, login.password)

    token = AuthController.create_token(self, login)

    app = ApplicationController()

    app.start(token)
