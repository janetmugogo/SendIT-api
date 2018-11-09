users = []


class Users:
    def __init__(self):
        self.db = users

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

    def get_single_user(self, user_id):
        for user in self.db:
            if user['user_id'] == user_id:
                return user

# janet = Users()
# janet.save_user('denzel', 'denzelkanyi@gmail.com', '123', '123')
# print(janet.get_all_parcels())
# print(janet.db)
