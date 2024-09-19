import os


class Config:
    SECRET_KEY = os.getenv("KEY")  # Load the secret key from the .env file
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///expense_manager.db"  # Using SQLite for simplicity
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
