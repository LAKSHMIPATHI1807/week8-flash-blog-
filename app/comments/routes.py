from flask import redirect, url_for, flash
from flask_login import login_required, current_user
from app.comments import bp
from app.models import Comment, Post
from app import db
from app.comments.forms import CommentForm

@bp.route("/add/<int:post_id>", methods=["POST"])
@login_required
def add_comment(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, author=current_user, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        flash("Comment added!")
    return redirect(url_for("posts.post_detail", id=post_id))
