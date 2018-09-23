#!/usr/bin/env python

import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

from common.common import connectToDb, closeDb

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank!'
                       )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        return {'message': 'Item {} not found'.format(name)}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'An item with name \"{}\" already exists.'.format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])

        try:
            item.insert()
        except Exception as err:
            return {'message': 'An error occurred inserting the item -> {}'.format(err)}, 500 # Internal server error

        return item.json(), 201

    def delete(self, name):
        connection, cursor = connectToDb()

        query = 'DELETE FROM items WHERE name=?'
        cursor.execute(query, (name,))

        closeDb(connection, commit=True)

        item_check = ItemModel.find_by_name(name)

        if item_check:
            return {'message': 'Deletion failed!!'}
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])

        if item is None:
            try:
                updated_item.insert()
            except:
                return {'message': 'An error occurred inserting the item'}, 500
        else:
            try:
                updated_item.update()
            except:
                return {'message': 'An error occurred updating the item'}, 500
        return updated_item.json()


class ItemList(Resource):
    def get(self):
        connection, cursor = connectToDb()

        query = 'SELECT * FROM items'
        result = cursor.execute(query)

        items = result.fetchall()

        closeDb(connection)

        return {'items': items}