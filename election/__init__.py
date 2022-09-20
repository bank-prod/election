from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
app = Flask(__name__)
app.config['ENV'] = 'development' 
app.config['SECRET_KEY'] = "ateyethtiklsbkibrom45d758gfj444gh77y4444"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/test.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/project.sqlite3"
# initialize the app with the extension
# db.init_app(app)
db = SQLAlchemy(app)
from election import models
from election import routes