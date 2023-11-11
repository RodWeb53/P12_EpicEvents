"""Module calcul des informations du menu"""


class MenuEntry:
    """Recupération de la class menuentry dans la classe menu"""
    def __init__(self, option, handler):
        self.option = option
        self.handler = handler


class Menu:
    """Menu"""
    def __init__(self):
        # création d'un dictionnaire vide dans une variable privée
        self._entries = {}
        # création du numéro de clé de base dans une variable privé
        self._autokey = 1

    def add(self, key, option, handler):
        """Fonction pour créer les clées"""
        # Si le numero de clé est sur auto boucle pour la création de la clé
        if key == "auto":
            key = str(self._autokey)
            self._autokey += 1
        # ajout des entrées dans le tableau _entries
        self._entries[str(key)] = MenuEntry(option, handler)

    # Fonction pour avoir acces aux option sans toucher au
    # dictionnaire _entries qui est privé dans les vues
    def items(self):
        """Fonction pour récupérer les entrées"""
        return self._entries.items()

    # Méthodes __contains__ pour gérer l'opérateur
    # in dans le choix utilisateur de views
    def __contains__(self, choice):
        return str(choice) in self._entries

    # Simulation d'un dictionnaire pour le controle du choix dans views
    def __getitem__(self, choice):
        return self._entries[choice]
