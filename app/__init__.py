from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from dotenv import load_dotenv
from .account import routes as account
from .category import routes as category
from .transaction import routes as transaction
from .user import routes as user

# Load environment variables
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Registering blueprints
    app.register_blueprint(account.account_bp)
    app.register_blueprint(category.category_bp)
    app.register_blueprint(transaction.transaction_bp)
    app.register_blueprint(user.user_bp)

    return app
