from app import ma


class TransactionSchema(ma.Schema):
    """
    Marshmallow schema for serializing Transaction objects.

    This schema defines the fields that should be included when
    serializing and deserializing transaction data, ensuring that only
    the specified fields are returned.

    Meta class:
        - `fields`: A tuple specifying the fields to include in the schema.

    Fields:
        - id: Transaction ID
        - amount: Transaction amount
        - date: Date of the transaction
        - description: Description of the transaction
        - user_id: ID of the user associated with the transaction
        - account_id: ID of the account associated with the transaction
        - category_id: ID of the category associated with the transaction
    """

    class Meta:
        fields = (
            "id",
            "amount",
            "date",
            "description",
            "user_id",
            "account_id",
            "category_id",
            "is_income",
        )
