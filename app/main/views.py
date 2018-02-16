from flask import render_template, request, redirect, url_for, abort,session
from . import main
from ..models import User, Post,Comment
from .forms import PostForm,CommentsForm
from .. import db

from flask_login import login_user, logout_user, login_required, current_user
# from ..email import mail_message


@main.route('/',methods=['GET','POST'])
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to Blogger'

    form = PostForm()

    if form.validate_on_submit():
        post = Post(body=form.body.data, title=form.title.data, author=current_user._get_current_object())
        post.save_post()
        return redirect(url_for('.index'))

    posts = Post.query.order_by(Post.timestamp.desc()).all()

    return render_template('index.html', form=form, posts=posts)


@main.route('/user/<username>')
@login_required
def user(username):
    """View function that returns the homepage for a particular user when they sign in"""
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)

    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('user.html', user=user, posts=posts)


@main.route('/post/<int:id>')
@login_required
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('posts.html', posts=[post])



@main.route('/addpost/', methods=['GET','POST'])  
def addpost():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, title=form.title.data, author=current_user._get_current_object())
        post.save_post()
        return redirect(url_for('.index'))
    return render_template('write.html', form=form)


@main.route('/pitch/comment/new/<int:id>',methods = ['GET','POST'])

def new_comment(id):
    form = CommentsForm()
  
    if form.validate_on_submit():
        new_comment = Comment(posts_id =id,comment=form.comment.data)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    
    return render_template('comment.html',comment_form=form)


