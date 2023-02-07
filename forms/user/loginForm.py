from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = EmailField('Correo', validators=[Email(), InputRequired()])
    password = PasswordField('Contraseña', validators=[InputRequired()])
