from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref="user", uselist=False)
    fecha = db.Column(db.DateTime)

    def __init__(self, title, body, idUser, fecha):
        self.title = title
        self.body = body
        self.id_user = idUser
        self.fecha = fecha
