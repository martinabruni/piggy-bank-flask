from app import ma


class TransactionSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "amount",
            "date",
            "description",
            "user_id",
            "account_id",
            "category_id",
        )
