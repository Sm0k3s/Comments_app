"""Tests for Comments app"""
import unittest
from  comments import Comments

class TestComments(unittest.TestCase):
    def SetUp(self):
        self.comment = {
            'message': 'dummy '
        }

    def test_comment_isnt_empty():
        empty = {'':''}
        Comment.create(empty)
        assert(len(message) > 0)


    def test_delete_comment():
        


