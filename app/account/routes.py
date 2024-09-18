from flask import Blueprint


# Defining a blueprint
account_bp = Blueprint(
    "account_bp", __name__, template_folder="templates", static_folder="static"
)
