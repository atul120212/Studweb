import flask
import db


class User(db.Document):
    email = db.StringField()
    password = db.StringField()