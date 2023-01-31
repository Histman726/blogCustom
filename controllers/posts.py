from flask import (
    render_template, Blueprint, flash, redirect, request, session, url_for,
)
from app import db

postURL = Blueprint('posts', __name__)


@postURL.route('/')
@postURL.route('/index')
def index():
    return render_template('posts/index.html')
