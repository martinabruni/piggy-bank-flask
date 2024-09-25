import os


class Config:
    """
    Base configuration class. Defines default settings and environment variables.

    Attributes:
        SECRET_KEY (str): Secret key used for session management.
        SQLALCHEMY_DATABASE_URI (str): URI for connecting to the SQLite database.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag to disable SQLAlchemy event tracking.
        SESSION_COOKIE_SECURE (bool): Enables secure cookies for session management.
        REMEMBER_COOKIE_SECURE (bool): Enables secure cookies for "Remember Me" functionality.
    """

    SECRET_KEY = os.getenv("KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///expense_manager.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True


class TestingConfig(Config):
    """
    Configuration class for testing. Inherits from the base Config class.

    Attributes:
        TESTING (bool): Flag to enable testing mode.
        SQLALCHEMY_DATABASE_URI (str): URI for an in-memory SQLite database.
        WTF_CSRF_ENABLED (bool): Disable CSRF protection for testing.
    """

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False


config = {
    "development": Config,
    "testing": TestingConfig,
}
