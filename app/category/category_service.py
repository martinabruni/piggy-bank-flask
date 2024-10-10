from app.category.category_model import Category
from app.category.category_serializer import CategorySchema
from app.utils.db_utils import find_records_by_filter


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

    def getCategories(self) -> CategorySchema.dump:
        categories = find_records_by_filter(Category)
        return self.__categoriesSchema.dump(categories)
