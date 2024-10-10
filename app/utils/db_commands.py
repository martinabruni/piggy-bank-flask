from datetime import datetime, timedelta
import random
from flask import Flask

from app.account.account_model import Account
from app.category.category_model import Category
from app.transaction.transaction_model import Transaction


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

    @app.cli.command("db_seed")
    def db_seed():
        # Define random categories
        categories = [
            "Food",
            "Entertainment",
            "Clothing",
            "Work",
            "Health",
            "Education",
        ]

        # Create and seed categories if not already present
        for category_name in categories:
            category = Category.query.filter_by(name=category_name).first()
            if not category:
                category = Category(name=category_name)
                db.session.add(category)

        db.session.commit()

        # Create accounts for the users
        accounts = [
            {
                "name": "Bank Account",
                "balance": round(random.uniform(500, 10000), 2),
                "user_id": 1,
            },
            {
                "name": "Credit Card",
                "balance": round(random.uniform(-1000, 5000), 2),
                "user_id": 1,
            },
            {
                "name": "PayPal",
                "balance": round(random.uniform(100, 5000), 2),
                "user_id": 1,
            },
            {
                "name": "Bank Account",
                "balance": round(random.uniform(500, 10000), 2),
                "user_id": 2,
            },
            {
                "name": "Credit Card",
                "balance": round(random.uniform(-1000, 5000), 2),
                "user_id": 2,
            },
            {
                "name": "PayPal",
                "balance": round(random.uniform(100, 5000), 2),
                "user_id": 2,
            },
        ]

        # Insert accounts into the database
        for acc_data in accounts:
            account = Account(
                name=acc_data["name"],
                balance=acc_data["balance"],
                user_id=acc_data["user_id"],
            )
            db.session.add(account)

        db.session.commit()  # Commit to get the account IDs

        # Fetch the created accounts and categories
        all_accounts = Account.query.all()
        all_categories = Category.query.all()

        # Generate random transactions for each account
        for account in all_accounts:
            # Number of transactions to generate per account
            num_transactions = random.randint(5, 10)

            for _ in range(num_transactions):
                # Create a random transaction
                amount = round(
                    random.uniform(-500, 1500), 2
                )  # Transaction can be expense or income
                description = f"Random transaction for account {account.name}"
                transaction_date = datetime.utcnow() - timedelta(
                    days=random.randint(1, 365)
                )  # Random date within the last year
                category = random.choice(all_categories)

                # Create and add the transaction
                transaction = Transaction(
                    amount=amount,
                    date=transaction_date,
                    description=description,
                    user_id=account.user_id,
                    account_id=account.id,
                    category_id=category.id,
                )

                db.session.add(transaction)

        # Final commit for the transactions
        db.session.commit()
