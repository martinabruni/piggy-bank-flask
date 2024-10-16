from app import db


class Category(db.Model):
    """
    Category model representing a transaction category.

    Attributes:
        id (int): Primary key for the category.
        name (str): Name of the category, must be unique and non-nullable.
    """

    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    is_income = db.Column(db.Boolean, nullable=False)
