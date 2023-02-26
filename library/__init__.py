from flask import Flask, request, Blueprint
from library.books.controller import books
from library.model import *

def create_bd():
    db.create_all()
    

def create_app(config_file = "config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = app.config['SQLALCHEMY_TRACK_MODIFICATIONS']
    app.register_blueprint(books)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
