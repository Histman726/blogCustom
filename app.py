from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return


if __name__ == '__main__':
    app.run()
    with app.app_context():
        db.create_all()
