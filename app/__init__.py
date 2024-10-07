# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

# from flask_wtf.csrf import CSRFProtect

# csrf = CSRFProtect()

# Load environment variables
load_dotenv()

# Create login instance
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

# Create db and migrations
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


from app.user.user_model import User


@login_manager.user_loader
def load_user(user_id):
    """Load a user from the database by user ID."""
    return User.query.get(int(user_id))


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.utils.db_commands import add_db_commands

    add_db_commands(app=app)
    # csrf.init_app(app)

    from .account import account_routes
    from .transaction import transaction_routes
    from .category import category_routes
    from .user.routes import user_routes
    from .user.routes import auth_routes

    # Registering blueprints
    app.register_blueprint(account_routes.account_bp)
    app.register_blueprint(category_routes.category_bp)
    app.register_blueprint(transaction_routes.transaction_bp)
    app.register_blueprint(user_routes.user_bp)
    app.register_blueprint(auth_routes.auth_bp)

    return app
