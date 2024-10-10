from app.transaction.transaction_model import Transaction
from app.transaction.transaction_serializer import TransactionSchema
from app.utils.db_utils import find_records_by_filter


class TransactionService:
    def __init__(self):
        self.__transactionSchema = TransactionSchema()
        self.__transactionsSchema = TransactionSchema(many=True)

    @property
    def transactionSchema(self):
        return self.__transactionSchema

    @property
    def transactionsSchema(self):
        return self.__transactionsSchema

    def getUserTransactions(self, user_id: int):
        lis = find_records_by_filter(Transaction, user_id=user_id)
        return self.__transactionsSchema.dump(lis)

    def getThisUserTransaction(self, user_id: int, transaction_id: int):
        result = find_records_by_filter(Transaction, user_id=user_id, id=transaction_id)
        return self.__transactionSchema.dump(result[0])
