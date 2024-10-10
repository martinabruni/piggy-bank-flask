from flask import jsonify
from app.category.category_model import Category
from app.category.category_serializer import CategorySchema
from app.utils.db_utils import find_record_by_id, find_records_by_filter


class CategoryService:
    def __init__(self):
        self.__categorySchema = CategorySchema()
        self.__categoriesSchema = CategorySchema(many=True)

    @property
    def categorySchema(self) -> CategorySchema:
        return self.__categorySchema

    @property
    def categoriesSchema(self) -> CategorySchema:
        return self.__categoriesSchema

    def getCategories(self):
        categories = find_records_by_filter(Category)
        return self.__categoriesSchema.dump(categories)

    def getThisCategory(self, category_id: int) -> Category:
        category = find_record_by_id(Category, category_id)
        return self.__categorySchema.dump(category)
