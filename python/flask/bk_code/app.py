#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'drrukus'
api = Api(app)

jwt = JWT(app, authenticate, identity) # creates /auth endpoint

items = []


class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price', 
		type=float,
		required=True,
		help='This field cannot be left blank!'
	)

	@jwt_required()
	def get(self, name):
		return {'item': next(filter(lambda i: i['name'] == name, items), None)}

	def post(self, name):
		if next(filter(lambda i: i['name'] == name, items), None):
			item = {'message': 'An item with name "{}" already exists.'.format(name)}
			status = 400
		else:
			data = Item.parser.parse_args()

			item = {'name': name, 'price': data['price']}
			items.append(item)
			status = 201
		return item, status

	def delete(self, name):
		global items
		items = list(filter(lambda x: x['name'] != name, items))
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
		return {'items': items}

api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/item/
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)

