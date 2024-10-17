from app import ma


class AccountSchema(ma.Schema):
    """
    Marshmallow schema for serializing Account objects.

    This schema defines the fields that should be included when
    serializing and deserializing account data.

    Meta class:
        - `fields`: A tuple specifying the fields to include in the schema.

    Fields:
        - id: Account ID
        - name: Account name
        - balance: Account balance
        - user_id: ID of the user associated with the account
    """

    class Meta:
        fields = ("id", "name", "balance", "user_id", "initial_balance")
