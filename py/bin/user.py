from security.encode import Encode

class User:
    id = 0
    name = ''
    password = ''

    def __init__(self, id, user, encode):
        self.name = user
        self.id = id
        self.password = encode.hash_password('pass')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
