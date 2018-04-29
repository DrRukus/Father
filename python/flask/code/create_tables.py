#!/usr/bin/env python

import sqlite3

from common.common import connectToDb, closeDb

connection, cursor = connectToDb()

#create_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)'
#cursor.execute(create_table)

#create_table = 'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)'
#cursor.execute(create_table)

queries = ['CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)',
           'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)']

for query in queries:
	cursor.execute(query)

closeDb(connection, commit=True)