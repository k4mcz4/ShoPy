import os.path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()

project_dir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)

    db_path = os.path.join(project_dir, 'db.sqlite')

    app.config['SECRET_KEY'] = b'(\xb49\xac\x1b\xe7=:\x81Q\xae\xfd+]\xbf\xe2\x05\x8c\xc4k0~\xb8\x85'
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from .models import User
        db.create_all()
        migrate.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
