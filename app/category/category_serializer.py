from app import ma


class CategorySchema(ma.Schema):
    """
    Marshmallow schema for serializing Category objects.

    This schema defines the fields to be included when serializing and
    deserializing category data.

    Meta class:
        - `fields`: A tuple specifying the fields to include in the schema.

    Fields:
        - id: Category ID
        - name: Category name
    """

    class Meta:
        fields = ("id", "name", "is_income")
