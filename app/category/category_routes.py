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
    """
    Route to retrieve all categories.

    Returns:
        JSON response containing all categories if the user is authenticated,
        otherwise returns an error message with a 401 Unauthorized status.
    """
    if current_user.is_authenticated:
        return jsonify(categories=catService.getCategories())
    else:
        return jsonify(error="User is not authenticated"), 401


@category_bp.route("/category/<int:category_id>", methods=["GET"])
def category(category_id: int):
    """
    Route to retrieve a single category by its ID.

    Args:
        category_id (int): The ID of the category to retrieve.

    Returns:
        JSON response containing the specified category if the user is authenticated,
        otherwise returns an error message with a 401 Unauthorized status.
    """
    if current_user.is_authenticated:
        return jsonify(category=catService.getThisCategory(category_id=category_id))
    else:
        return jsonify(error="User is not authenticated"), 401


@category_bp.route("/categories/is_income/<string:is_income>", methods=["GET"])
def category_type(is_income: str):
    if current_user.is_authenticated:
        return jsonify(categories=catService.getCategoriesType(is_income))
    else:
        return jsonify(error="User is not authenticated"), 401
