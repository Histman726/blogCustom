from flask import (
    render_template, Blueprint, flash, redirect, request, session, url_for,
)
from flask_login import login_user
from app import db, loginManager
from forms.user.registerForm import RegisterForm
from models.userDB import User


@loginManager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


usersURL = Blueprint('users', __name__, url_prefix='/auth')


@usersURL.route('/register', methods=['GET', 'POST'])
def registro():
    form = RegisterForm(meta={'csrf': False})

    if form.validate_on_submit():
        user = User(nombre=form.nombre.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for('posts.index'))

    return render_template('users/register.html', form=form)


@usersURL.route('/login')
def login():
    return render_template('users/login.html')
