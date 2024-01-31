from flask_login import UserMixin
from sqlalchemy import ForeignKeyConstraint

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
    stock_take_inventory = db.relationship('StockTakeInventory', backref='parent')


class StockTakeInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_take_id = db.Column(db.Integer, db.ForeignKey('stock_take.id'))
    product_barcode = db.Column(db.Integer)
    insert_date = db.Column(db.DateTime)
    __table_args__ = (
        ForeignKeyConstraint([stock_take_id], [StockTake.id], name='stock_take_id_fkey'),
    )
