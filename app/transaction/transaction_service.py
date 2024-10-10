from app.transaction.transaction_model import Transaction
from app.transaction.transaction_serializer import TransactionSchema
from app.utils.db_utils import find_records_by_filter


class TransactionService:
    """
    Service class to manage Transaction operations, including retrieving and
    serializing user transactions from the database.

    This class provides methods to retrieve single or multiple transactions
    for a user and serialize the data.

    Attributes:
        __transactionSchema (TransactionSchema): Schema for serializing a single transaction.
        __transactionsSchema (TransactionSchema): Schema for serializing multiple transactions.
    """

    def __init__(self):
        """
        Initializes the TransactionService with schemas for serializing
        individual and multiple transactions.
        """
        self.__transactionSchema = TransactionSchema()
        self.__transactionsSchema = TransactionSchema(many=True)

    @property
    def transactionSchema(self):
        return self.__transactionSchema

    @property
    def transactionsSchema(self):
        return self.__transactionsSchema

    def getUserTransactions(self, user_id: int):
        """
        Retrieves all transactions associated with a specific user.

        Args:
            user_id (int): The ID of the user whose transactions are to be retrieved.

        Returns:
            dict: Serialized data of all user transactions.
        """
        lis = find_records_by_filter(Transaction, user_id=user_id)
        return self.__transactionsSchema.dump(lis)

    def getThisUserTransaction(self, user_id: int, transaction_id: int):
        """
        Retrieves a specific transaction for a user by transaction ID.

        Args:
            user_id (int): The ID of the user whose transaction is to be retrieved.
            transaction_id (int): The ID of the transaction to retrieve.

        Returns:
            dict: Serialized data of the specified user transaction.
        """
        result = find_records_by_filter(Transaction, user_id=user_id, id=transaction_id)
        return self.__transactionSchema.dump(result[0])
