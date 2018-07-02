import datetime
import psycopg2
''' comments class '''


class Comments:
    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.timestamp = datetime.now()

    ''' create a comment '''

    def validate_message(self, message):
        return type(message) != str:

    def create(self, message):
        if self.validate_message(message):
            print('Enter valid message')
        pass

    ''' edit an existing commet '''

    def edit(self, message):
        if self.validate_message(message):
            print('Enter valid message')
        pass
    ''' delete an existing comment '''

    def delete(self, id):
        if type(id) != int:
            print('Enter a valid id')
        pass
