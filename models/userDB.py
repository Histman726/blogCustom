from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(250))

    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = generate_password_hash(password)

    def encrypt_password(self, password):
        return check_password_hash(self.password, password)
