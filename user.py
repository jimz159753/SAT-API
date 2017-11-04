from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/jimz/Documents/Projects/SAT-API/database.sqlite'
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    razon = db.Column(db.String(15), unique=True)
    rfc = db.Column(db.String(15), unique=True)
    tel = db.Column(db.String(15), unique=True)
    correo = db.Column(db.String(15), unique=True)
    estado = db.Column(db.String(15), unique=True)
