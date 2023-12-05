"""Module views pour la modification des clients"""
from utils.clean_screen import clear
from rich.console import Console
from rich.table import Table


class UpdateClientMenuView:
    """Update client menu views"""
    def __init__(self, menu):
        self.menu = menu

    # Création d'une méthodes pour afficher le menu
    def _display_menu(self):
        clear()
        print("")
        table = Table(title="Menu modification des clients", width=80, style="green", show_lines=True)

        table.add_column("N°", style="cyan", width=10, justify="center")
        table.add_column("Fonctionnalité", style="cyan", width=70)

        for key, entry in self.menu.items():
            table.add_row(f"{key}", f"{entry.option}")

        console = Console()
        console.print(table)

    def get_user_choice(self):
        """Boucle pour afficher tant que l'utilisateur n'a pas fait de bon choix"""
        while True:
            # Afficher le menu à l'utilisateur
            self._display_menu()
            # Demander à l'utilisateur de faire un choix
            choice = input("Entrez votre choix >> ")
            # Valider le choix de l'utilisateur
            if choice in self.menu:
                # Retourner le choix de l'utilisateur
                return self.menu[choice]
