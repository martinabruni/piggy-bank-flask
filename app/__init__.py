from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from dotenv import load_dotenv
from .account import routes as account
from .category import routes as category
from .transaction import routes as transaction
from .user import routes as user
from flask_bcrypt import Bcrypt
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

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


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Registering blueprints
    app.register_blueprint(account.account_bp)
    app.register_blueprint(category.category_bp)
    app.register_blueprint(transaction.transaction_bp)
    app.register_blueprint(user.user_bp)

    return app
