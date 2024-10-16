from app.user.user_model import User
from app.user.user_serializer import UserSchema
from app.utils.db_utils import find_record_by_id


class ProfileService:
    def __init__(self) -> None:
        self.__userSchema = UserSchema()

    def getProfileDetails(self, user_id: int):
        user = find_record_by_id(User, user_id)
        return self.__userSchema.dump(user)
