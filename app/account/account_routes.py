from flask import Blueprint, jsonify, redirect, request
from app.account.account_form import AccountForm
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
    
    
@account_bp.route("/account/new", methods=["POST"])
def new_account():
    form = AccountForm(request.form)

    if not current_user.is_authenticated:
        return jsonify({"error": "User is not authenticated"}), 401

    if form.validate_on_submit():
        form_data = form.data  
        account_name = form_data.get('name')
        initial_balance = form_data.get('initial_balance') or 0.0

        
        new_account = accountService.createAccount(
            user_id=current_user.id,
            name=account_name,
            initial_balance=initial_balance
        )

        if new_account:
            return jsonify({
                "message": "Account created successfully",
                "account": new_account
            }), 201
        else:
            return jsonify({"error": "Account creation failed"}), 500

    return jsonify({"errors": form.errors}), 400


@account_bp.route("/account/delete/<int:account_id>", methods=["DELETE"])
def delete_account(account_id: int):
    if not current_user.is_authenticated:
        return jsonify({"error": "User is not authenticated"}), 401

    success = accountService.deleteAccount(user_id=current_user.id, account_id=account_id)

    if success:
        return jsonify({"message": "Account deleted successfully"}), 200
    else:
        return jsonify({"error": "Account deletion failed"}), 500