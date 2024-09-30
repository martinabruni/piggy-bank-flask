import pytest
from app import create_app, db


@pytest.fixture(scope="module")
def test_app():
    """
    Fixture for creating the Flask test application.

    Yields:
        Flask application configured for testing.
    """
    app = create_app("testing")

    with app.app_context():
        yield app


@pytest.fixture(scope="module")
def test_client(test_app):
    """
    Fixture for creating the test client.

    Args:
        test_app: The test Flask application.

    Returns:
        Flask test client for sending requests to the application.
    """
    return test_app.test_client()


@pytest.fixture(scope="module")
def init_database(test_app):
    """
    Fixture for initializing the test database.

    Yields:
        Initialized test database.
    """
    db.create_all()

    yield db

    db.session.remove()
    db.drop_all()
