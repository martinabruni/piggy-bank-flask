from app.account.account_model import Account
from app.account.account_serializer import AccountSchema
from app.utils.db_utils import find_records_by_filter


class AccountService:
    """
    Service class to manage Account operations, including retrieving and
    serializing user accounts from the database.

    This class encapsulates the logic for interacting with Account data and
    provides methods to get single or multiple accounts for a user, returning
    the serialized output.

    Attributes:
        __accountSchema (AccountSchema): Schema for serializing a single account.
        __accountsSchema (AccountSchema): Schema for serializing multiple accounts.
    """

    def __init__(self):
        """
        Initializes the AccountService with schemas for serializing
        individual and multiple accounts.
        """
        self.__accountSchema = AccountSchema()
        self.__accountsSchema = AccountSchema(many=True)

    @property
    def accountSchema(self):
        return self.__accountSchema

    @property
    def accountsSchema(self):
        return self.__accountsSchema

    def getUserAccounts(self, user_id: int):
        """
        Retrieves all accounts associated with a specific user.

        Args:
            user_id (int): The ID of the user whose accounts are to be retrieved.

        Returns:
            dict: Serialized data of all user accounts.
        """
        lis = find_records_by_filter(Account, user_id=user_id)
        return self.__accountsSchema.dump(lis)

    def getThisUserAccount(self, user_id: int, account_id: int):
        """
        Retrieves a specific account for a user by account ID.

        Args:
            user_id (int): The ID of the user whose account is to be retrieved.
            account_id (int): The ID of the account to retrieve.

        Returns:
            dict: Serialized data of the specific user account.
        """
        result = find_records_by_filter(Account, user_id=user_id, id=account_id)
        return self.__accountSchema.dump(result[0])
