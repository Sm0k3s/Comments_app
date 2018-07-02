from _datetime import datetime
import psycopg2
from db import queries, utils
import os

con = utils.connect_db('comments_app', 'postgres', 'password')


class Comments:
    def __init__(self, author, text, parent_id=None):
        self.author = author
        self.text = text
        self.parent_id = parent_id
        utils.query_db(con, queries.add_comment, (author, text, parent_id))

    @staticmethod
    def list_comments():
        comments = utils.query_db(con, queries.get_comments, ())
        return comments

    @staticmethod
    def get_comment(comment_id):
        comments = utils.query_db(con, queries.get_comment, (id,))
        return comments

    @staticmethod
    def edit(comment_id, message):

        comment = utils.query_db(con, queries.get_comment, (comment_id,))
        role = utils.query_db(con, queries.check_previledge, (os.getenv('user_id')))

        if role[0]['previledge'] == 'moderator' or role[0]['previledge'] == 'admin' or comment[0][
            'author'] == os.getenv('user_id'):
            args = (message, datetime.now(), comment_id)
            comments = utils.query_db(con, queries.edit_comment, args)
            return comments

    @staticmethod
    def delete(comment_id):
        comment = utils.query_db(con, queries.get_comment, (comment_id,))
        role = utils.query_db(con, queries.check_previledge, (os.getenv('user_id')))
        if type(id) != int:
            print('Enter a valid id')
        try:
            if role[0]['previledge'] == 'moderator' or role[0]['previledge'] == 'admin' or comment[0][
                'author'] == os.getenv('user_id'):
                comment = utils.query_db(con, queries.delete_comment, (comment_id,))
                return comment
        except:
            raise Exception("error deleting comment")
