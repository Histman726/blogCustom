from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

DATABASE_URI = 'postgresql+psycopg2://postgres:2486@localhost:5432/blog'
DATABASE_URI_TEST = 'sqlite:///blog.sqlite'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI_TEST
db = SQLAlchemy(app)
app.secret_key = 'BLOG_CUSTOM'
loginManager = LoginManager(app)


from controllers.posts import postURL
app.register_blueprint(postURL)

from controllers.users import usersURL
app.register_blueprint(usersURL)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run()
