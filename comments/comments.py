from _datetime import datetime
import psycopg2


class Comments:
    def __init__(self, author, text, parent_id=None):
        self.author = author
        self.text = text
        self.parent_id = parent_id


    @staticmethod
    def list_comments():
        pass

    @staticmethod
    def get_comment(comment_id):
        pass

    @staticmethod
    def edit(comment_id, message):
        pass

    @staticmethod
    def delete(comment_id):
        if type(id) != int:
            print('Enter a valid id')
        try:
            pass
        except:
            pass
