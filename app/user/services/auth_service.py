from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user
from app.user.models.user import User
from app.utils.db_utils import find_records_by_filter, add_record


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
        self.bcrypt = bcrypt

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
        hashed_password = self.bcrypt.generate_password_hash(password).decode("utf-8")
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
            if self.bcrypt.check_password_hash(user.password_hash, password):
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
