from app import db
from app.models import User, Post, Comment

def test_user_password_hashing(app):
    user = User(username="lakshmi", email="lakshmi@test.com")
    user.set_password("mypassword")

    assert user.check_password("mypassword")
    assert not user.check_password("wrongpass")


def test_post_creation(app):
    user = User(username="author", email="author@test.com")
    user.set_password("pass")
    db.session.add(user)
    db.session.commit()

    post = Post(title="Test Post", content="Test Content", author=user)
    db.session.add(post)
    db.session.commit()

    assert post in user.posts
    assert post.title == "Test Post"


def test_comment_relationship(app):
    user = User(username="commenter", email="c@test.com")
    user.set_password("pass")
    db.session.add(user)

    post = Post(title="Post", content="Content", author=user)
    db.session.add(post)
    db.session.commit()

    comment = Comment(content="Nice post!", author=user, post=post)
    db.session.add(comment)
    db.session.commit()

    assert comment in post.comments
    assert comment.author.username == "commenter"
