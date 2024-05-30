from flask import Flask, url_for
from os import path
import os
from dotenv import load_dotenv
from flask_login import LoginManager, current_user
from flask_mail import Mail

# import mysql.connector
from flask_sqlalchemy import SQLAlchemy as sql

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd = "FlavorTown281195!",
#     database = 'testdb'
# )

db = sql()



load_dotenv()
application = Flask(__name__)
application.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
application.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(application)
application.config.from_pyfile('config.py')
mail = Mail(application)

from .views import views
from .auth import auth 
from .models import User

application.register_blueprint(views, url_prefix='/')
application.register_blueprint(auth, url_prefix='/')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(application)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


