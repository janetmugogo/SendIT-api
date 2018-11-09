users = []


class Users:
    def __init__(self):
        self.db = users

    # the user creates an account and their details are saved/stored in the dictionary
    def save_user(self, username, email, password, confirm_password):
        new_user = {
            'user_id': len(self.db) + 1,
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
            'admin': False
        }
        self.db.append(new_user)


