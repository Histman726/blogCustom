from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired


class CreateForm(FlaskForm):
    title = StringField('Titulo del post', validators=[InputRequired()])
    body = TextAreaField('Contenido del post', validators=[InputRequired()])
