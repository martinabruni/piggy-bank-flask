from flask import Blueprint, jsonify
from flask_login import current_user

from app.transaction.transaction_service import TransactionService


# Defining a blueprint
transaction_bp = Blueprint(
    "transaction_bp", __name__, template_folder="templates", static_folder="static"
)


transactionService = TransactionService()


@transaction_bp.route("/transactions", methods=["GET"])
def accounts():
    if current_user.is_authenticated:
        return jsonify(
            user_accounts=transactionService.getUserTransactions(current_user.id)
        )
    else:
        return jsonify(error="User is not authenticated"), 401


@transaction_bp.route("/transaction/<int:transaction_id>", methods=["GET"])
def account(transaction_id: int):
    if current_user.is_authenticated:
        return jsonify(
            user_accounts=transactionService.getThisUserTransaction(
                current_user.id, transaction_id=transaction_id
            )
        )
    else:
        return jsonify(error="User is not authenticated"), 401
