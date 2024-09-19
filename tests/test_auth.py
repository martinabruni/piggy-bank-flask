def test_register(test_client, init_database):
    response = test_client.post(
        "/register",
        data={
            "username": "testuser",
            "email": "testuser@example.com",
            "pwd": "password123",
            "cpwd": "password123",
        },
    )
    assert response.status_code == 201  # Adjust according to expected status code


def test_login(test_client, init_database):
    response = test_client.post(
        "/login", data={"email": "testuser@example.com", "pwd": "password123"}
    )
    assert response.status_code == 200  # Adjust according to expected status code


def test_logout(test_client, init_database):
    response = test_client.post("/logout")
    assert response.status_code == 200  # Assuming a redirect after logout
