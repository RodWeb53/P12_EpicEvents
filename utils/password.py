import bcrypt


class Password():

    def __init__(self):
        pass

    def hash_password(self, password):
        """Cryptage du mot de passe avec bcrypt"""
        bytes = password.encode('utf8')

        salt = bcrypt.gensalt()

        hash = bcrypt.hashpw(bytes, salt)

        hash = hash.decode("utf8")

        return hash

    def verify_password(self, password, mdp_de_la_base):
        """Vérification du mot de passe saisie et celui de la base de données"""

        password = password.encode('utf8')

        print(bcrypt.checkpw(password, mdp_de_la_base.encode("utf8")))

        if bcrypt.checkpw(password, mdp_de_la_base.encode("utf8")):
            print("match")
            print("Le mot de passe est correcte")
            return 1
        else:
            print("does not match")
            print("Le mot de passe est incorecte")
            return 2

        # result = bcrypt.checkpw(hash, mdp_de_la_base)

        # print("les donnes de decrypt")
        # print(result)

        # return result
