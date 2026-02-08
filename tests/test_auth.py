from app import db
from app.models import User


def test_register(client, app):
    response = client.post("/auth/register", data={
        "username": "newuser",
        "email": "new@test.com",
        "password": "password",
        "password2": "password"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert User.query.filter_by(username="newuser").first() is not None


def test_login_logout(client, app):
    user = User(username="loginuser", email="login@test.com")
    user.set_password("password")
    db.session.add(user)
    db.session.commit()

    # Login
    response = client.post("/auth/login", data={
        "username": "loginuser",
        "password": "password"
    }, follow_redirects=True)

    assert b"Logout" in response.data

    # Logout
    response = client.get("/auth/logout", follow_redirects=True)
    assert b"Login" in response.data
