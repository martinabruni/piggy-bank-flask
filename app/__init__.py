from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from dotenv import load_dotenv
from app.models.user import User
from app.models.account import Account
from app.models.category import Category
from app.models.transaction import Transaction


# from app.routes import main_blueprint

# Load environment variables
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # app.register_blueprint(main_blueprint)

    return app
