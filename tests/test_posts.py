from app import db
from app.models import User, Post, Comment


def login(client, username, password):
    return client.post("/auth/login", data={
        "username": username,
        "password": password
    }, follow_redirects=True)


def test_create_post(client, app):
    user = User(username="poster", email="poster@test.com")
    user.set_password("pass")
    db.session.add(user)
    db.session.commit()

    login(client, "poster", "pass")

    response = client.post("/posts/create", data={
        "title": "My Post",
        "content": "Post content"
    }, follow_redirects=True)

    assert b"My Post" in response.data


def test_add_comment(client, app):
    user = User(username="commenter", email="c@test.com")
    user.set_password("pass")
    db.session.add(user)

    post = Post(title="Post", content="Content", author=user)
    db.session.add(post)
    db.session.commit()

    login(client, "commenter", "pass")

    response = client.post(f"/posts/post/{post.id}", data={
        "content": "Great post!"
    }, follow_redirects=True)

    assert b"Great post!" in response.data
