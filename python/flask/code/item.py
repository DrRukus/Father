#!/usr/bin/env python

import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

DATA_DB = 'data.db'

def connectToDb(db):
	cnx = sqlite3.connect(db)
	return cnx, cnx.cursor()

class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price', 
		type=float,
		required=True,
		help='This field cannot be left blank!'
	)

	@jwt_required()
	def get(self, name):
		item = Item.find_by_name(name)

		if item:
			return item
		return {'message': 'Item {} not found'.format(name)}, 404

	@classmethod
	def find_by_name(cls, name):
		connection, cursor = connectToDb(DATA_DB)

		query = 'SELECT * FROM items WHERE name=?'
		result = cursor.execute(query, (name,))
		row = result.fetchone()
		connection.close()

		if row:
			return {'item': {'name': row[0], 'price': row[1]}}

	def post(self, name):
		if Item.find_by_name(name):
			return {'message': 'An item with name "{}" already exists.'.format(name)}, 400

		data = Item.parser.parse_args()

		item = {'name': name, 'price': data['price']}

		connection, cursor = connectToDb(DATA_DB)

		query = 'INSERT INTO items VALUES (?, ?)'

		cursor.execute(query, (item['name'], item['price']))

		connection.commit()
		connection.close()

		return item, 201

	def delete(self, name):
		connection, cursor = connectToDb(DATA_DB)

		query = 'DELETE FROM items WHERE name=?'
		result = cursor.execute(query, (name,))
		print('Result: {}'.format(dir(result)))

		query = 'SELECT * FROM items WHERE name=?'
		result = cursor.execute(query, (name,))

		if result.fetchone():
			return {'message': 'Deletion failed!!!!!'}
		return {'message': 'Item deleted'}

	def put(self, name):
		data = Item.parser.parse_args()

		item = next(filter(lambda x: x['name'] == name, items), None)
		if item is None:
			item = {'name': name, 'price': data['price']}
			items.append(item)
		else:
			item.update(data)
		return item


class ItemList(Resource):
	def get(self):
		connection, cursor = connectToDb(DATA_DB)

		query = 'SELECT * FROM items'
		result = cursor.execute(query)

		items = result.fetchall()

		connection.commit()
		connection.close()

		return {'items': items}