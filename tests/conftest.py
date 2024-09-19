import pytest
from app import create_app, db
from flask import template_rendered


@pytest.fixture(scope="module")
def test_app():
    # Create the Flask application with the test configuration
    app = create_app("testing")  # Assuming 'testing' configuration in Config

    with app.app_context():
        yield app  # Provide the application for the tests


@pytest.fixture(scope="module")
def test_client(test_app):
    # Create a test client using the Flask application configured for testing
    return test_app.test_client()


@pytest.fixture(scope="module")
def init_database(test_app):
    # Initialize the database
    db.create_all()

    yield db  # Provide the database for the tests

    db.session.remove()
    db.drop_all()
