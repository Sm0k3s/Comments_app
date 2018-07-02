''' users class'''


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def edit_comment(self, id):
        if self.validate_id(id):
            print('Enter a valid id')

    def validate_id(self):
        return if type(id) != int:


''' Moderators class'''


class Moderator(User):
    def __init__(self):
        pass

    def edit_comment(self, id):
        if self.validate_id(id):
            print('Enter a valid id')

        try:
            pass
        except:
            pass

    def delete_comment(self, id):
        if self.validate_id(id):
            print('Enter a valid id')
        try:
            pass
        except:
            pass


class Admin(User):
    def __init__(self):
        try:
            pass
        except:
            pass

    def edit_comment(self, id):
        if self.validate_id(id):
            print('Enter a valid id')

        try:
            pass
        except:
            pass

    def delete_comment(self, id):
        if self.validate_id(id):
            print('Enter a valid id')

        try:
            pass
        except:
            pass
