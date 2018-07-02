-- create a users table
CREATE TABLE public.users
(
  id       serial PRIMARY KEY,
  username varchar(50)             NOT NULL,
  created  timestamp DEFAULT now() NOT NULL,
  password varchar(50)             NOT NULL,
  updated  timestamp
);
COMMENT ON TABLE public.users
IS 'A table containing all users';

--create previleges type enum
CREATE TYPE previledge AS ENUM ('user', 'moderator', 'admin');

-- create previledges table
create table previledges
(
  id         serial                  not null
    constraint previledges_pkey
    primary key,
  user_id    integer                 not null
    constraint previledges_users_id_fk
    references users
    on update cascade on delete cascade,
  previledge previledge              not null,
  created    timestamp default now() not null,
  updated    timestamp
);

-- create a comments table
create table comments
(
  id      serial                  not null
    constraint comments_pkey
    primary key,
  author  integer                 not null,
  text    varchar(500)            not null,
  created timestamp default now() not null,
  updated timestamp
);

comment on table comments
is 'the table to store comments';

