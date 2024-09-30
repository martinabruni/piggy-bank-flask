from app import db


class Account(db.Model):
    """
    Account model representing a user's account.

    Attributes:
        id (int): Primary key for the account.
        name (str): Name of the account.
        balance (float): Balance of the account, defaults to 0.0.
        user_id (int): Foreign key linking to the user who owns the account.
    """

    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float, default=0.0)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
