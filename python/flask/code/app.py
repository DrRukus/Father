#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'drrukus'
api = Api(app)

jwt = JWT(app, authenticate, identity) # creates /auth endpoint

items = []


class Item(Resource):
	@jwt_required()
	def get(self, name):
		#item = next(filter(lambda i: i['name'] == name, items), None)
		#return item, 200 if item else 404 
		return {'item': next(filter(lambda i: i['name'] == name, items), None)}

	def post(self, name):
		if next(filter(lambda i: i['name'] == name, items), None):
			item = {'message': 'An item with name "{}" already exists.'.format(name)}
			status = 400
		else:
			data = request.get_json()
			item = {'name': name, 'price': data['price']}
			items.append(item)
			status = 201
		return item, status


class ItemList(Resource):
	def get(self):
		return {'items': items}

api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/item/
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)