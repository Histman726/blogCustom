from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired


class EditForm(FlaskForm):
    title = StringField('Titulo: ', validators=[InputRequired()])
    body = TextAreaField('Contenido: ', validators=[InputRequired()])
