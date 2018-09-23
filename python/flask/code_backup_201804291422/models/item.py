#!/usr/bin/env python

import sqlite3

from db import db
from common.common import connectToDb, closeDb


class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        connection, cursor = connectToDb()

        query = 'SELECT * FROM items WHERE name=?'
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        closeDb(connection)

        item = cls(*row[1:]) if row else None

        return item

    def insert(self):
        connection, cursor = connectToDb()

        query = 'INSERT INTO items VALUES (NULL, ?, ?)'
        result = cursor.execute(query, (self.name, self.price))

        closeDb(connection, commit=True)

    def update(self):
        connection, cursor = connectToDb()

        query = 'UPDATE items SET price=? WHERE name=?'
        cursor.execute(query, (self.price, self.name))

        closeDb(connection, commit=True)
