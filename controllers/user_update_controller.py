"""Module controller du Update menu Utilisateur"""
from controllers import menu_update_user_controller
from models.employe import CustomUser
from utils.user import UtilsUser
from views.update_user_view import UpdateUserView
from sqlalchemy.orm import sessionmaker
from database import engine
from utils.validate import Validate


class UpdateUserController:
    """Menu controller pour l'update du user"""

    def __init__(self, token):
        self.session = sessionmaker(bind=engine)
        self.user = CustomUser
        self.view = UpdateUserView()
        self.token = token

    def update_user_first_name(self, token):
        """Modification dans la BD du first_name"""
        verify = True
        while verify:
            # Demande du N° d'utilisateur à modifier
            choice = UtilsUser.display_menu_user_choice_modify(self)
            # vérification que l'utilisateur est connue
            session = self.session()
            user = session.query(CustomUser).filter_by(id=choice).first()
            session.close()
            if user is not None:
                verify = False

        # Demande du nouveau first_name
        first_name_update = self.view.update_first_name()
        # Sauvegarde du first_name dans la BD
        session = self.session()
        user = session.query(CustomUser).filter_by(id=choice).first()
        user.first_name = first_name_update
        session.commit()
        session.close()
        validate = "Le prénom à été modifié avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def update_user_last_name(self, token):
        """Modification dans la BD du last_name"""
        verify = True
        while verify:
            # Demande du N° d'utilisateur à modifier
            choice = UtilsUser.display_menu_user_choice_modify(self)
            # vérification que l'utilisateur est connue
            session = self.session()
            user = session.query(CustomUser).filter_by(id=choice).first()
            session.close()
            if user is not None:
                verify = False

        # Demande du nouveau last_name
        last_name_update = self.view.update_last_name()
        # Sauvegarde du last_name dans la BD
        session = self.session()
        user = session.query(CustomUser).filter_by(id=choice).first()
        user.last_name = last_name_update
        session.commit()
        session.close()
        validate = "Le nom à été modifié avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def update_user_email(self, token):
        """Modification dans la BD de l'email"""
        verify = True
        while verify:
            # Demande du N° d'utilisateur à modifier
            choice = UtilsUser.display_menu_user_choice_modify(self)
            # vérification que l'utilisateur est connue
            session = self.session()
            user = session.query(CustomUser).filter_by(id=choice).first()
            session.close()
            if user is not None:
                verify = False

        # Demande du nouvel email
        email_update = self.view.update_email()
        # Sauvegarde de l'email dans la BD
        session = self.session()
        user = session.query(CustomUser).filter_by(id=choice).first()
        user.email = email_update
        session.commit()
        session.close()
        validate = "L'email' à été modifié avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def update_user_phone(self, token):
        """Modification dans la BD du phone"""
        verify = True
        while verify:
            # Demande du N° d'utilisateur à modifier
            choice = UtilsUser.display_menu_user_choice_modify(self)
            # vérification que l'utilisateur est connue
            session = self.session()
            user = session.query(CustomUser).filter_by(id=choice).first()
            session.close()
            if user is not None:
                verify = False

        # Demande du nouveau N° de phone
        phone_update = self.view.update_phone()
        # Sauvegarde du phone dans la BD
        session = self.session()
        user = session.query(CustomUser).filter_by(id=choice).first()
        user.phone = phone_update
        session.commit()
        session.close()
        validate = "Le téléphone fixe à été modifié avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def update_user_phone_mobile(self, token):
        """Modification dans la BD du phone_mobile"""
        verify = True
        while verify:
            # Demande du N° d'utilisateur à modifier
            choice = UtilsUser.display_menu_user_choice_modify(self)
            # vérification que l'utilisateur est connue
            session = self.session()
            user = session.query(CustomUser).filter_by(id=choice).first()
            session.close()
            if user is not None:
                verify = False

        # Demande du nouveau N° de phone_mobile
        phone_mobile_update = self.view.update_phone_mobile()
        # Sauvegarde du phone_mobile dans la BD
        session = self.session()
        user = session.query(CustomUser).filter_by(id=choice).first()
        user.phone_mobile = phone_mobile_update
        session.commit()
        session.close()
        validate = "Le téléphone mobile à été modifié avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def update_user_role(self, token):
        """Modification dans la BD du role"""
        verify = True
        while verify:
            # Demande du N° d'utilisateur à modifier
            choice = UtilsUser.display_menu_user_choice_modify(self)
            # vérification que l'utilisateur est connue
            session = self.session()
            user = session.query(CustomUser).filter_by(id=choice).first()
            session.close()
            if user is not None:
                verify = False

        # Demande du nouveau role
        role_update = self.view.update_role()
        # Sauvegarde du role dans la BD
        session = self.session()
        user = session.query(CustomUser).filter_by(id=choice).first()
        user.role_id = role_update
        session.commit()
        session.close()
        validate = "Le role à été modifié avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def update_user_is_active(self, token):
        """Modification dans la BD du is_active"""
        verify = True
        while verify:
            # Demande du N° d'utilisateur à modifier
            choice = UtilsUser.display_menu_user_choice_modify(self)
            # vérification que l'utilisateur est connue
            session = self.session()
            user = session.query(CustomUser).filter_by(id=choice).first()
            session.close()
            if user is not None:
                verify = False

        # Demande de is_active
        is_active_update = self.view.update_is_active()
        # Sauvegarde de is_active dans la BD
        session = self.session()
        user = session.query(CustomUser).filter_by(id=choice).first()
        user.is_active = is_active_update
        session.commit()
        session.close()
        validate = "L'activation' à été modifiée avec succès dans la bd"
        Validate.validate_bd(self, validate)
        return self.menu_back(self.token)

    def menu_back(self, token):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_update_user_controller.UpdateUserMenuController(token)
        return self.handler
