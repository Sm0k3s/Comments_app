import os
import click

from users.users import User
from comments.comments import Comments


def signup(username, password, role = None, *args, **kwargs):
    user_obj = User(username, password, role)
    print('Account created : username {} '.format(user_obj.username))


def require_login(fn):
    def inner(*args, **kwargs):
        try:
            user = User.get_user(os.environ['user_id'])
        except Exception:
            print('You are not logged in')

        return fn(*args, **kwargs)

    return inner


def login(username, password, *args, **kwargs):
    user = User.get_user(username)
    if user.password == password:
        os.environ['username'] = user.username
        os.environ['user_id'] = user.id
        print('Logged in')
    else:
        print('Invalid login credentials')


@require_login
def logout(*args, **kwargs):
    if os.environ.get('username') and os.environ.get('user_id'):
        os.environ.pop('username')
        os.environ.pop('user_id')
    print('Logged out')


@require_login
def create_comment(author_id, text, parent_id, *args, **kwargs):
    comment = Comments(author_id, text, parent_id)
    print('Comment created: Text: {}\nComment id: {}'.format(comment.text, comment.id))


@require_login
def edit_comment(comment_id, text, *args, **kwargs):
    new_comment = Comments.edit(comment_id, text)
    print('Comment updated: \nText: {}\nComment id: {}'.format(new_comment.text, new_comment.id))


@require_login
def list_comments(*args, **kwargs):
    all_comments = Comments.list_comments()
    for comment in all_comments:
        print('Id: {}, Text: {}'.format(comment.id, comment.text))


@require_login
def delete(comment_id, *args, **kwargs):
    Comments.delete(comment_id)


@require_login
def reset_priviledge(*args, **kwargs):
    pass


commands = {
    'signup': signup,
    'login': login,
    'logout': logout,
    'createcomment': create_comment,
    'editcomment': edit_comment,
    'listcomments': list_comments,
    'delete': delete,
    'resetpriviledge': reset_priviledge
}


@click.command()
@click.option('--record')
@click.option('--author_id')
@click.option('--parent_id')
@click.option('--text')
@click.option('--comment_id')
@click.option('--data')
@click.option('--username')
@click.option('--password')
@click.argument('cmdl')
def execute(cmdl, record = None, data = None, username = None, password=None,
            author_id = None, parent_id=None, text=None, comment_id=None):
    try:
        commands[cmdl](record = record, data=data, username = username, password=password,
                       comment_id = comment_id, text = text, parent_id =parent_id, author_id=author_id)
    except KeyError:
        print('Unknown command')


if __name__ == '__main__':
    execute()