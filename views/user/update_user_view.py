from utils.update_user import UtilsUpdateUser
from utils.clean_screen import clear


class UpdateUserView:

    def __init__(self):
        self.utils_user = UtilsUpdateUser

    def update_first_name(self):
        clear()
        first_name_update = self.utils_user.display_menu_update_first_name(self)
        return first_name_update

    def update_last_name(self):
        clear()
        last_name_update = self.utils_user.display_menu_update_last_name(self)
        return last_name_update

    def update_email(self):
        clear()
        email_update = self.utils_user.display_menu_update_email(self)
        return email_update

    def update_phone(self):
        clear()
        phone_update = self.utils_user.display_menu_update_phone(self)
        return phone_update

    def update_phone_mobile(self):
        clear()
        phone_update = self.utils_user.display_menu_update_phone_mobile(self)
        return phone_update

    def update_role(self):
        clear()
        role_update = self.utils_user.display_menu_update_role(self)
        return role_update

    def update_is_active(self):
        clear()
        is_active_update = self.utils_user.display_menu_update_is_active(self)
        return is_active_update
