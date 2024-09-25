def test_register(test_client, init_database):
    """
    Test the user registration endpoint.

    Sends a POST request with valid registration data and asserts the response.

    Args:
        test_client: The test client.
        init_database: The initialized test database.
    """
    response = test_client.post(
        "/register",
        data={
            "username": "testuser",
            "email": "testuser@example.com",
            "pwd": "password123",
            "cpwd": "password123",
        },
    )
    assert response.status_code == 201


def test_login(test_client, init_database):
    """
    Test the user login endpoint with valid credentials.

    Sends a POST request with valid login data and asserts the response.

    Args:
        test_client: The test client.
        init_database: The initialized test database.
    """
    response = test_client.post(
        "/login", data={"email": "testuser@example.com", "pwd": "password123"}
    )
    assert response.status_code == 200


def test_logout(test_client, init_database):
    """
    Test the user logout endpoint.

    Sends a POST request and asserts the response.

    Args:
        test_client: The test client.
        init_database: The initialized test database.
    """
    response = test_client.post("/logout")
    assert response.status_code == 200


def test_login_wrong_email(test_client, init_database):
    """
    Test the login endpoint with an invalid email.

    Sends a POST request with incorrect email data and asserts the response.

    Args:
        test_client: The test client.
        init_database: The initialized test database.
    """
    response = test_client.post(
        "/login", data={"email": "testuserfail@example.com", "pwd": "password123"}
    )
    assert response.status_code == 401


def test_login_wrong_password(test_client, init_database):
    """
    Test the login endpoint with an invalid password.

    Sends a POST request with incorrect password data and asserts the response.

    Args:
        test_client: The test client.
        init_database: The initialized test database.
    """
    response = test_client.post(
        "/login", data={"email": "testuser@example.com", "pwd": "wrongpassword"}
    )
    assert response.status_code == 401
