from app import db
from datetime import datetime


class Transaction(db.Model):
    """
    Transaction model representing a financial transaction.

    Attributes:
        id (int): Primary key for the transaction.
        amount (float): Amount of money involved in the transaction.
        date (datetime): Date of the transaction, defaults to the current UTC time.
        description (str): Optional description of the transaction.
        user_id (int): Foreign key linking to the user who made the transaction.
        account_id (int): Foreign key linking to the associated account.
        category_id (int): Foreign key linking to the associated category.
    """

    __tablename__ = "transaction"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
