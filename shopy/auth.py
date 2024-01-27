from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/password')
@login_required
def password_change():
    return render_template('password.html')


@auth.route('/signup')
def signup():
    users = User.query.all()
    if not users:
        return render_template('signup.html')
    else:
        return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')

    new_user = User(username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect('main.profile')


@auth.route('/password', methods=['POST'])
def password_change_post():
    pass


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('login.html')
