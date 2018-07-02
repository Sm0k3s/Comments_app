add_user = """insert into users(username,password) values (%s,%s);"""
add_previledge = """
insert into previledges(user_id, previledge) values (%s,%s)"""
add_comment = """insert into comments(author, text, parent) values (%s,%s,%s)"""

get_user = """select * from users where  username = %s;"""
get_comment = """select * from comments where id = %s;"""
get_children = """select * from comments where parent =%s"""


edit_comment = """"""