from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.posts import bp
from app.models import Post, Comment
from app import db
from app.posts.forms import PostForm, CommentForm

@bp.route("/create", methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Post created!")
        return redirect(url_for("main.index"))
    return render_template("posts/create_post.html", form=form)

@bp.route("/post/<int:post_id>")
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    
    
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You must be logged in to comment.")
            return redirect(url_for('auth.login'))

        comment = Comment(
            content=form.content.data,
            author=current_user,
            post=post
        )
        db.session.add(comment)
        db.session.commit()
        flash("Comment added successfully!")
        return redirect(url_for('posts.post_detail', id=id))
    
    return render_template("posts/post_detail.html", post=post, form=form)

@bp.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_post(id):
    post = Post.query.get_or_404(id)
    if post.author != current_user:
        flash("You cannot edit this post.")
        return redirect(url_for("main.index"))

    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Post updated!")
        return redirect(url_for("posts.post_detail", id=post.id))
    return render_template("posts/create_post.html", form=form)

@bp.route("/<int:id>/delete")
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    if post.author == current_user:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted.")
    return redirect(url_for("main.index"))
