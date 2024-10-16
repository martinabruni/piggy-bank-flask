from flask import Blueprint, jsonify, redirect
from flask_login import current_user

from app.account.account_service import AccountService


# Defining a blueprint
account_bp = Blueprint(
    "account_bp", __name__, template_folder="templates", static_folder="static"
)

accountService = AccountService()


@account_bp.route("/accounts", methods=["GET"])
def accounts():
    """
    Route to retrieve all accounts of the authenticated user.

    Returns:
        JSON response containing the user's accounts if authenticated,
        otherwise returns an error message with a 401 Unauthorized status.
    """
    if current_user.is_authenticated:
        return jsonify(user_accounts=accountService.getUserAccounts(current_user.id))
    else:
        return jsonify(error="User is not authenticated"), 401


@account_bp.route("/account/<int:account_id>", methods=["GET"])
def account(account_id: int):
    """
    Route to retrieve a specific account by its ID for the authenticated user.

    Args:
        account_id (int): The ID of the account to retrieve.

    Returns:
        JSON response containing the specified user's account if authenticated,
        otherwise returns an error message with a 401 Unauthorized status.
    """
    if current_user.is_authenticated:
        return jsonify(
            user_accounts=accountService.getThisUserAccount(
                current_user.id, account_id=account_id
            )
        )
    else:
        return jsonify(error="User is not authenticated"), 401
