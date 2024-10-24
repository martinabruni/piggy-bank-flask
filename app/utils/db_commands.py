from datetime import datetime, timedelta
import random
import click
from flask import Flask

from app.account.account_model import Account
from app.category.category_model import Category
from app.transaction.transaction_model import Transaction
from app.user.user_model import User


def add_db_commands(app: Flask):
    """
    Adds custom database commands to the Flask CLI for managing the database.

    Commands:
        - `db_create`: Creates all database tables based on the models.
        - `db_drop`: Drops all database tables.
        - `db_seed`: Seeds the database with sample data:
            - Predefined categories (e.g., "Food", "Entertainment").
            - Randomly generated accounts for two users.
            - Random transactions associated with accounts and categories.

    Args:
        app (Flask): The Flask application instance.

    Example usage:
    ```bash
    flask db_create   # Creates the database
    flask db_drop     # Drops the database
    flask db_seed     # Seeds the database with sample data
    ```
    """
    from app import db

    @app.cli.command("db_create")
    def db_create():
        db.create_all()
        print("Database created!")

    @app.cli.command("db_drop")
    def db_drop():
        db.drop_all()
        print("Database dropped!")

    @app.cli.command("drop_table")
    @click.argument("table_name")
    def drop_table(table_name):
        """
        CLI command to drop a table by name.

        Usage: flask drop_table <table_name>
        """
        # Mapping table names to their models
        models = {
            "account": Account,
            "transaction": Transaction,
            "category": Category,
            "user": User,
        }

        # Get the model class dynamically
        model = models.get(table_name.lower())

        if model:
            # Drop the table
            model.__table__.drop(db.engine)
            print(f"Table '{table_name}' dropped successfully!")
        else:
            print(
                f"Table '{table_name}' not found. Available tables are: {', '.join(models.keys())}"
            )

    @app.cli.command("db_seed")
    def db_seed():
        # Create 5 predefined categories
        categories = [
            "Food",
            "Entertainment",
            "Clothing",
            "Work",
            "Health",
            "Refund",
            "Transfer",
        ]

        # Seed categories if not already present
        for category_name in categories:
            category = Category.query.filter_by(name=category_name).first()
            if not category:
                category = Category(name=category_name)
                db.session.add(category)

        # Commit categories to the database
        db.session.commit()

        # Fetch users to create accounts for them
        users = User.query.all()

        for user in users:
            # Create 2 accounts for each user
            accounts = [
                {
                    "name": f"{user.username}'s Bank Account",
                    "initial_balance": round(random.uniform(500, 10000), 2),
                    "user_id": user.id,
                },
                {
                    "name": f"{user.username}'s Credit Card",
                    "initial_balance": round(random.uniform(-1000, 5000), 2),
                    "user_id": user.id,
                },
            ]

            # Insert accounts into the database
            for acc_data in accounts:
                account = Account(
                    name=acc_data["name"],
                    initial_balance=acc_data["initial_balance"],
                    user_id=acc_data["user_id"],
                )
                db.session.add(account)

        # Commit accounts to the database
        db.session.commit()

        print("Database seeded with users, accounts, and categories!")

    @app.cli.command("db_add_transaction")
    def db_add_transaction():
        """
        CLI command to add 2 transactions for each account of every user.
        The transactions will have random amounts and dates within the last 30 days.
        """
        users = User.query.all()

        # Fetch a random category to associate with transactions
        categories = Category.query.all()

        if not categories:
            print("No categories available. Please seed categories first.")
            return

        for user in users:
            for account in user.accounts:
                for _ in range(2):  # Add 2 transactions per account
                    description = f"Auto-generated transaction for {account.name}"
                    transaction_date = datetime.utcnow() - timedelta(
                        days=random.randint(1, 30)
                    )  # Random date within last 30 days
                    category = random.choice(categories)  # Choose a random category
                    amount = round(random.uniform(-1500, 1500), 2)  # Random amount
                    if amount > 0:
                        is_income = True
                    else:
                        is_income = False

                    transaction = Transaction(
                        amount=amount,
                        date=transaction_date,
                        description=description,
                        user_id=user.id,
                        account_id=account.id,
                        category_id=category.id,
                        is_income=is_income,
                    )

                    # Add transaction to session
                    db.session.add(transaction)

        # Commit all transactions
        db.session.commit()

        print("Added 2 transactions for each account of every user.")
