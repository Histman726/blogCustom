from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.sqlite'
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
