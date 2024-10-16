from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """
    User model representing a registered user in the system.

    Attributes:
        id (int): Primary key for the user.
        username (str): Username of the user, must be unique and non-nullable.
        email (str): Email address of the user, must be unique and non-nullable.
        password_hash (str): Hashed password for the user.
    """

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
