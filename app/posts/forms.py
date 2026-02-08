from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Submit")

class CommentForm(FlaskForm):
    content = TextAreaField("Write a comment...", validators=[DataRequired()])
    submit = SubmitField("Post Comment")