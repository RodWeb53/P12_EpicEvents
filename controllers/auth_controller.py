"""Module controller d'authentification des users"""
from models.employe import CustomUser
from database import engine
from sqlalchemy.orm import sessionmaker
import jwt
import datetime
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class AuthController:
    """Menu controller pour la vérification des users"""

    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        self.user = CustomUser

    def create_token(self, login):
        secret_key = os.environ.get("SECRET_KEY")
        payload = {
            'last_name': login.last_name,
            'first_name': login.first_name,
            'role_id': login.role_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return token

    def decrypt_token(self, token):
        secret_key = os.environ.get("SECRET_KEY")
        valeur = jwt.decode(token, secret_key, algorithms=["HS256"])
        print("les valeurs de token décrypté")
        print(valeur)
        return valeur
