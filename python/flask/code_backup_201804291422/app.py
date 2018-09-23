#!/usr/bin/env python

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'drrukus'
API = Api(app)

jwt = JWT(app, authenticate, identity) # creates /auth endpoint

API.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/item/
API.add_resource(ItemList, '/items')
API.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
