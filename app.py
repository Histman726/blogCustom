from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


from posts import postURL
app.register_blueprint(postURL)

from users import usersURL
app.register_blueprint(usersURL)


if __name__ == '__main__':
    app.run()
    with app.app_context():
        db.create_all()
