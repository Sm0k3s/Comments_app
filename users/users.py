''' users class'''
from db import utils, queries
import os

con = utils.connect_db('comments_app', 'postgres', 'password')


class User:
    def __init__(self, username, password, role='user'):
        self.username = username
        self.password = password
        user = utils.query_db(con, queries.add_user, (username, password))
        id = user[0]['id']
        role = utils.query_db(con, queries.add_previledge, (id, role))

    #
    # def edit_user(self, username, password):
    #     pass

    @staticmethod
    def list_users():
        user = utils.query_db(con, queries.get_users, ())
        return user

    @staticmethod
    def get_user(username):
        user = utils.query_db(con, queries.get_user, (username,))
        return user

    @staticmethod
    def user_login(username, password):
        user = utils.query_db(con, queries.user_login, (username, password))
        if len(user) != 1:
            print("user not logged in")
            return
        return user
