import datetime

from flask import (
    render_template, Blueprint, flash, redirect, request, session, url_for,
)
from flask_login import current_user

from app import db
from forms.post.createForm import CreateForm
from forms.post.editForm import EditForm
from models.postDB import Post
from utilities.gets import get_user, get_post

postURL = Blueprint('posts', __name__)


@postURL.route('/')
@postURL.route('/index')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts, author=get_user, current_user=current_user)


@postURL.route('/blog/create', methods=['GET', 'POST'])
def create():
    if current_user.id is None:
        return redirect(url_for('users.login'))

    form = CreateForm(meta={'csrf': False})

    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, idUser=current_user.id, fecha=datetime.datetime.now())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts.index'))

    return render_template('posts/create.html', form=form)


@postURL.route('/blog/edit/<id>', methods=['GET', 'POST'])
def edit(id=None):
    form = EditForm(meta={'csrf': False})
    post = get_post(id, check_author=False)

    if form.validate_on_submit() and not post is None:
        post.title = form.title.data
        post.body = request.form.get('body')
        db.session.commit()
        return redirect(url_for('posts.index'))

    return render_template('posts/edit.html', form=form, post=post)
