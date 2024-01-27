from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)


class StockTake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)


class StockTakeInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_take_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
