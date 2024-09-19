from flask import Blueprint


# Defining a blueprint
transaction_bp = Blueprint(
    "transaction_bp", __name__, template_folder="templates", static_folder="static"
)
