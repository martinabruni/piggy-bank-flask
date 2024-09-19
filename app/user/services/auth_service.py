from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app.user.models.user import User
from app.utils.db_utils import find_records_by_filter, add_record, delete_record


class AuthService:
    def __init__(self, bcrypt: Bcrypt):
        self.bcrypt = bcrypt

    def register_user(self, username: str, email: str, password: str) -> User:
        hashed_password = self.bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(username=username, email=email, password_hash=hashed_password)
        add_record(new_user)
        return new_user

    def authenticate_user(self, email: str, password: str) -> bool:
        user = find_records_by_filter(User, email=email)
        if user:
            user = user[0]  # Assuming unique email
            if check_password_hash(user.password_hash, password):
                return user
        return None

    def login(self, user: User):
        login_user(user)

    def logout(self):
        logout_user()
