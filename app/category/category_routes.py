from flask import Blueprint, jsonify, request
from flask_login import current_user

from app.category.category_service import CategoryService

# Defining a blueprint
category_bp = Blueprint(
    "category_bp", __name__, template_folder="templates", static_folder="static"
)

catService = CategoryService()


@category_bp.route("/categories", methods=["GET"])
def categories():
    if current_user.is_authenticated:
        return jsonify(categories=catService.getCategories())
