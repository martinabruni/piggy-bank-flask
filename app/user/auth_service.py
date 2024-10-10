from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user
from app.user.user_model import User
from app.utils.db_utils import delete_record, find_records_by_filter, add_record


class AuthService:
    """
    Service class for handling user authentication and authorization.

    Attributes:
        bcrypt (Bcrypt): Instance of Flask-Bcrypt for hashing passwords.
    """

    def __init__(self, bcrypt: Bcrypt):
        """
        Initialize AuthService with a bcrypt instance.
        """
        self.__bcrypt = bcrypt

    def register_user(self, username: str, email: str, password: str) -> User:
        """
        Register a new user by hashing their password and saving the user to the database.

        Args:
            username (str): The chosen username of the user.
            email (str): The email address of the user.
            password (str): The user's plain-text password.

        Returns:
            User: The newly created user object.
        """
        hashed_password = self.__bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(username=username, email=email, password_hash=hashed_password)
        add_record(new_user)
        self.login(new_user)
        return new_user

    def authenticate_user(self, email: str, password: str) -> User:
        """
        Authenticate a user by comparing their email and password.

        Args:
            email (str): The email address of the user.
            password (str): The plain-text password entered by the user.

        Returns:
            User: The authenticated user object, or None if authentication fails.
        """
        user = find_records_by_filter(User, email=email)
        if user:
            user = user[0]
            if self.__bcrypt.check_password_hash(user.password_hash, password):
                return user
        return None

    def login(self, user: User):
        """
        Log the user into the system.

        Args:
            user (User): The user object to log in.
        """
        login_user(user)

    def logout(self):
        """
        Log the user out of the system.
        """
        logout_user()

    def delete_user(self, email: str):
        """
        Deletes a user based on the provided email.

        Searches for a user with the given email. If found, the user is deleted from the
        database. Returns `True` if deletion is successful, otherwise `False` if no user
        is found.

        Args:
            email (str): The email address of the user to delete.

        Returns:
            bool:
                - `True` if the user is found and deleted.
                - `False` if no user with the provided email exists.
        """
        user = find_records_by_filter(User, email=email)
        if user:
            user = user[0]
            delete_record(user)
            return True
        else:
            return False
