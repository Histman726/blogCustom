from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    nombre = StringField('Nombre', validators=[InputRequired()])
    email = EmailField('Correo', validators=[Email(), InputRequired()])
    password = PasswordField('Contraseña', validators=[InputRequired(), EqualTo('confirm')])
    confirm = PasswordField('Confirmar contraseña', validators=[InputRequired()])
