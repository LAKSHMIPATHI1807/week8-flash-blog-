from flask import render_template, request, redirect, url_for, flash
from app.main import bp
from app.models import Post, User, Comment, Category
from sqlalchemy import func
from flask_login import login_required, current_user

@bp.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()

    stats = {
        "total_posts": Post.query.count(),
        "total_comments": Comment.query.count(),
        "total_categories": Category.query.count() if Category else 0,
        "popular_post": Post.query.order_by(Post.views.desc()).first()
    }

    active_users = User.query.all()

    return render_template(
        "main/index.html",
        posts=posts,
        stats=stats,
        active_users=active_users
    )
    
@bp.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")

    if not email:
        flash("Please enter an email address.", "danger")
        return redirect(url_for("main.index"))

    # For now we just show a success message
    # Later you can store emails in the database
    flash("Subscribed successfully!", "success")
    return redirect(url_for("main.index"))

@bp.route("/profile")
@login_required
def profile():
    return render_template("main/profile.html", user=current_user)


@bp.route("/search")
def search():
    query = request.args.get("q")

    if not query:
        results = []
    else:
        results = Post.query.filter(
            Post.title.contains(query) | Post.content.contains(query)
        ).all()

    return render_template("main/search_results.html", results=results, query=query)