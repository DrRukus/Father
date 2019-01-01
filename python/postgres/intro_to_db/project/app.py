#!/usr/bin/env python

from user import User

user = User(email = 'themouse@disney.com',
            first_name = 'Mickey',
            last_name = 'Mouse',
            id = None)

print('User object: {}'.format(user))

user.save_to_db()
