#!/usr/bin/env python

import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

DATA_DB = 'data.db'

def connectToDb(db):
	cnx = sqlite3.connect(db)
	return cnx, cnx.cursor()

def closeDb(cnx):
	cnx.commit()
	cnx.close()

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

		closeDb(connection)

		if row:
			return {'item': {'name': row[0], 'price': row[1]}}

	@classmethod
	def insert(cls, item):
		connection, cursor = connectToDb(DATA_DB)

		query = 'INSERT INTO items VALUES (?, ?)'
		cursor.execute(query, (item['name'], item['price']))

		closeDb(connection)

	@classmethod
	def update(cls, item):
		connection, cursor = connectToDb(DATA_DB)

		query = 'UPDATE items SET price=? WHERE name=?'
		cursor.execute(query, (item['price'], item['name']))

		closeDb(connection)

	def post(self, name):
		if Item.find_by_name(name):
			return {'message': 'An item with name "{}" already exists.'.format(name)}, 400

		item = {'name': name, 'price': Item.parser.parse_args()['price']}

		try:
			Item.insert(item)
		except:
			return {'message': 'An error occurred inserting the item.'}, 500 # Internal server error

		return item, 201

	def delete(self, name):
		connection, cursor = connectToDb(DATA_DB)

		query = 'DELETE FROM items WHERE name=?'
		result = cursor.execute(query, (name,))

		closeDb(connection)

		itemCheck = Item.find_by_name(name)

		if itemCheck:
			return {'message': 'Deletion failed!!!!!'}
		return {'message': 'Item deleted'}

	def put(self, name):
		data = Item.parser.parse_args()
		
		item = Item.find_by_name(name)
		updated_item = {'name': name, 'price': data['price']}

		if item is None:
			try:
				Item.insert(updated_item)
			except:
				return {'message': 'An error occurred inserting the item'}, 500
		else:
			try:
				Item.update(updated_item)
			except:
				return {'message': 'An error occurred updating the item'}, 500
		return updated_item


class ItemList(Resource):
	def get(self):
		connection, cursor = connectToDb(DATA_DB)

		query = 'SELECT * FROM items'
		result = cursor.execute(query)

		items = result.fetchall()

		closeDb(connection)

		return {'items': items}