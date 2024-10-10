from app import ma


class AccountSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "balance", "user_id")
