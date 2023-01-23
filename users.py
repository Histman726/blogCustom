from flask import (
    render_template, Blueprint, flash, redirect, request, session, url_for,
)
from app import db

usersURL = Blueprint('users', __name__, url_prefix='/auth')


@usersURL.route('/register')
def registro():
    return render_template('users/register.html')


@usersURL.route('/login')
def login():
    return render_template('users/login.html')
