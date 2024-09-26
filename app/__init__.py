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


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from .account.routes import account_routes
    from .transaction.routes import transaction_routes
    from .category.routes import category_routes
    from .user.routes import user_routes

    # Registering blueprints
    app.register_blueprint(account_routes.account_bp)
    app.register_blueprint(category_routes.category_bp)
    app.register_blueprint(transaction_routes.transaction_bp)
    app.register_blueprint(user_routes.user_bp)

    return app
