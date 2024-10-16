from flask import jsonify
from app.category.category_model import Category
from app.category.category_serializer import CategorySchema
from app.utils.db_utils import find_record_by_id, find_records_by_filter


class CategoryService:
    """
    Service class to manage Category operations, including retrieving and
    serializing categories from the database.

    This class encapsulates the logic for interacting with Category data and
    provides methods to get single or multiple categories, returning the
    serialized output.

    Attributes:
        __categorySchema (CategorySchema): Schema for serializing a single category.
        __categoriesSchema (CategorySchema): Schema for serializing multiple categories.
    """

    def __init__(self):
        """
        Initializes the CategoryService with schemas for serializing
        individual and multiple categories.
        """
        self.__categorySchema = CategorySchema()
        self.__categoriesSchema = CategorySchema(many=True)

    @property
    def categorySchema(self) -> CategorySchema:
        return self.__categorySchema

    @property
    def categoriesSchema(self) -> CategorySchema:
        return self.__categoriesSchema

    def getCategories(self):
        """
        Retrieves all categories from the database and returns serialized data.

        Returns:
            dict: Serialized data of all categories.
        """
        categories = find_records_by_filter(Category)
        return self.__categoriesSchema.dump(categories)

    def getThisCategory(self, category_id: int) -> Category:
        """
        Retrieves a single category by its ID and returns serialized data.

        Args:
            category_id (int): The ID of the category to retrieve.

        Returns:
            dict: Serialized data of the specified category.
        """
        category = find_record_by_id(Category, category_id)
        return self.__categorySchema.dump(category)
