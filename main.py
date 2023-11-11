"""Module main pour lancer l'application"""
from controllers.application_controller import ApplicationController

if __name__ == "__main__":
    print("le menu de login")
    retour = input("entrez votre choix")

    if retour == "login":
        print("Dans la boucle 1")
        app = ApplicationController()

        app.start()
    else:
        print("sortie")
