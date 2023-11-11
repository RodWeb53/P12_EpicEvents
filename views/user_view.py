from utils.user import UtilsUser
from utils.clean_screen import clear


class AddUserView:

    def __init__(self):
        self.utils_user = UtilsUser

    def new_user(self):
        new_user_add = {}
        create_entry = True
        clear()

        while create_entry:
            login = self.utils_user.display_menu_login(self)
            last_name = self.utils_user.display_menu_last_name(self)
            first_name = self.utils_user.display_menu_first_name(self)
            email = self.utils_user.display_menu_email(self)
            phone = self.utils_user.display_menu_phone(self)
            phone_mobile = self.utils_user.display_menu_phone_mobile(self)
            password = self.utils_user.display_menu_password(self)
            is_staff = False
            is_active = self.utils_user.display_menu_is_active(self)
            choice_user = self.utils_user.display_menu_user_choice_save(self)
            create_entry = False
        if choice_user == "o":
            new_user_add = {
                "login": str(login),
                "last_name": str(last_name),
                "first_name": str(first_name),
                "email": str(email),
                "phone": str(phone),
                "phone_mobile": str(phone_mobile),
                "password": str(password),
                "is_staff": is_staff,
                "is_active": is_active,
            }
            return new_user_add
        elif choice_user == "n":
            return -1
