import click


def signup(record = None, data=None):
    pass


def auth_login():
    pass


def login(record = None, data=None):
    pass


def logout(record = None, data=None):
    pass


def create_comment(record = None, data=None):
    pass


def edit_comment(record = None, data=None):
    pass


def list_comments(record = None, data=None):
    pass


def delete(record = None, data=None):
    pass


def reset_priviledge(record = None, data=None):
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
@click.option('--data')
@click.argument('cmdl')
def execute(cmdl, record, data):
    try:
        commands[cmdl](record = record, data=data)
    except KeyError:
        print('Unknown command')


if __name__ == '__main__':
    execute()