from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Required, Email, EqualTo
from ..models import User, Post
from wtforms import ValidationError

class PostForm(FlaskForm):
    title = TextAreaField("heading here",validators=[Required()])
    body = TextAreaField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')


class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment Here', validators=[Required()])
    submit = SubmitField('SUBMIT')  
