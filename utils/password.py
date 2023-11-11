import bcrypt


class Password():

    def __init__(self):
        pass

    def hash_password(self, password):
        """Cryptage du mot de passe avec bcrypt"""
        bytes = password.encode('utf8')

        salt = bcrypt.gensalt()

        hash = bcrypt.hashpw(bytes, salt)

        return hash

    def verify_password(self, password_entry, mdp_de_la_base):
        """Vérification du mot de passe saisie et celui de la base de données"""

        userBytes = password_entry.encode('utf-8')

        result = bcrypt.checkpw(userBytes, mdp_de_la_base)

        return result
