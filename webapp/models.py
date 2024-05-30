from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    

