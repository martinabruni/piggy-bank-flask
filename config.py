import os


class Config:
    SECRET_KEY = os.getenv("KEY")  # Load the secret key from the .env file
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///expense_manager.db"  # Using SQLite for simplicity
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    PREFERRED_URL_SCHEME = "https"
