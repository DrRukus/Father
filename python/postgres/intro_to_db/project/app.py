#!/usr/bin/env python

from database import Database
from user import User

Database.initialize(database = 'learning',
                    host = 'localhost',
                    user = 'postgres',
                    password = 'postgres',
                    port = 5433)

user_1 = User(email = 'therabbit@wb.com',
              first_name = 'Bugs',
              last_name = 'Bunny',
              id = None)

print('User object: {}'.format(user_1))

user_1.save_to_db()

user_from_db = User.load_from_db_by_email('therabbit@wb.com')
print(user_from_db)

user_2 = User(email = 'theduck@wb.com',
              first_name = 'Daffy',
              last_name = 'Duck',
              id = None)

print('User object: {}'.format(user_2))

user_2.save_to_db()
