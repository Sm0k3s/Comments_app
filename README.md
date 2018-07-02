# Comments_app

# Users:

    - Users come in 3 roles: normal users, moderators, and admins.

# Comments:

    - Comments are simply a message, a timestamp, and the author.
    - Comments can also be a reply, so we'll store what the parent comment was.

## _How it works_

### _User_

    - Users can create an account
    - Users can be logged in and out.
    - Users can create comments
    - Users can only edit their own comments

### _Moderator is a User_

    - Moderators can only edit their own comments
    - Moderators can delete any comments

### _Admin is both a User and a Moderator_

    - Admins can edit any comments
    - Admins can delete any comments

### _Comments contain a reference to the User who created it (author)_
