#!/usr/bin/env python

import psycopg2

class User(object):

    def __init__(self, email, first_name, last_name, id=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.columns = 'email, first_name, last_name'
        self.insert = 'INSERT INTO users ({}) VALUES (%s, %s, %s)'

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        with psycopg2.connect(database='learning',
                              user='postgres',
                              password='postgres',
                              host='localhost',
                              port=5433) as connection:

            with connection.cursor() as cursor:
                cursor.execute(self.insert.format(self.columns),
                               (self.email,
                                self.first_name,
                                self.last_name))
