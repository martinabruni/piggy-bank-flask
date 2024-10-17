from flask import Blueprint, jsonify
from flask_login import current_user

from app.transaction.transaction_service import TransactionService


# Defining a blueprint
transaction_bp = Blueprint(
    "transaction_bp", __name__, template_folder="templates", static_folder="static"
)


transactionService = TransactionService()


@transaction_bp.route("/transactions", methods=["GET"])
def transactions():
    """
    Route to retrieve all transactions of the authenticated user.

    Returns:
        JSON response containing the user's transactions if authenticated,
        otherwise returns an error message with a 401 Unauthorized status.
    """
    if current_user.is_authenticated:
        return jsonify(
            user_transactions=transactionService.getUserTransactions(current_user.id)
        )
    else:
        return jsonify(error="User is not authenticated"), 401


@transaction_bp.route("/transaction/<int:transaction_id>", methods=["GET"])
def transaction(transaction_id: int):
    """
    Route to retrieve a specific transaction by its ID for the authenticated user.

    Args:
        transaction_id (int): The ID of the transaction to retrieve.

    Returns:
        JSON response containing the specified user's transaction if authenticated,
        otherwise returns an error message with a 401 Unauthorized status.
    """
    if current_user.is_authenticated:
        return jsonify(
            user_transactions=transactionService.getThisUserTransaction(
                current_user.id, transaction_id=transaction_id
            )
        )
    else:
        return jsonify(error="User is not authenticated"), 401


@transaction_bp.route("/transactions/is_income/<string:is_income>", methods=["GET"])
def transactions_type(is_income: str):
    if current_user.is_authenticated:

        return jsonify(
            user_transactions=transactionService.getTransactionsType(
                current_user.id, is_income
            )
        )
    else:
        return jsonify(error="User is not authenticated"), 401
