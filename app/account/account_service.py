from app.account.account_model import Account
from app.account.account_serializer import AccountSchema
from app.utils.db_utils import find_records_by_filter


class AccountService:
    def __init__(self):
        self.__accountSchema = AccountSchema()
        self.__accountsSchema = AccountSchema(many=True)

    @property
    def accountSchema(self):
        return self.__accountSchema

    @property
    def accountsSchema(self):
        return self.__accountsSchema

    def getUserAccounts(self, user_id: int):
        lis = find_records_by_filter(Account, user_id=user_id)
        return self.__accountsSchema.dump(lis)

    def getThisUserAccount(self, user_id: int, account_id: int):
        result = find_records_by_filter(Account, user_id=user_id, id=account_id)
        return self.__accountSchema.dump(result[0])
