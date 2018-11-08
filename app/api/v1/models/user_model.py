users = []


class Users:
    def __init__(self):
        self.db = users


"""user can create an account and their details saved"""


def save_user(self, username, email, password, confirm_password):
    new_user = {
        'user_id': len(self.db) + 1,
        'username': username,
        'email': email,
        'password': password,
        'confirm_password': confirm_password,
        'status': "intransit"
    }
    self.db.append(new_user)

# janet = Users()
# janet.save_user('denzel', 'denzelkanyi@gmail.com', '123', '123')
#
# print(janet.db)
