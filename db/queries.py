add_user = """insert into users(username,password) values (%s,%s) returning *;"""
add_previledge = """insert into previledges(user_id, previledge) values (%s,%s) returning *"""
add_comment = """insert into comments(author, text, parent) values (%s,%s,%s) returning *"""
check_previledge = """select previledge from previledges where user_id = %s;"""

get_user = """select * from users where  username = %s;"""
get_users = """select * from users;"""
user_login = """select * from users where username=%s or password=%s;"""
get_comment = """select * from comments where id = %s;"""
get_comments = """select * from comments """
get_children = """select * from comments where parent =%s"""

edit_comment = """update comments set (text,updated ) = (%s,%s) where id=%s returning *;"""
delete_comment = """delete from comments where id = %s returning *;"""
