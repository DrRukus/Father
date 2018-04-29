#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
	def get(self, name):
		theItem = {'item': None}
		for item in items:
			if item['name'] == name:
				theItem = item
				status = 200
				break
		else:
			status = 404
		return theItem, status

	def post(self, name):
		data = request.get_json()
		item = {
			'name': name,
			'price': data['price']
			}
		items.append(item)
		return item, 201


class ItemList(Resource):
	def get(self):
		return {'items': items}

api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/item/
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)

