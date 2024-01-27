from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Product

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)


@main.route('/inventory')
@login_required
def inventory():
    return render_template('inventory.html')


@main.route('/products')
@login_required
def products():
    all_products = Product.query.all()

    return render_template('products.html', all_products=all_products)


@main.route('/products', methods=['POST'])
@login_required
def add_products():
    barcode = request.form.get('barcode')
    product_name = request.form.get('product-name')
    price = request.form.get('price')

    new_product = Product(barcode=barcode, name=product_name, price=price)
    db.session.add(new_product)
    db.session.commit()

    return redirect(url_for('main.products'))
