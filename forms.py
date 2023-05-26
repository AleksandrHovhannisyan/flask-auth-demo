from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()], render_kw={"autocomplete": "name", "aria-describedby": "username-errors"})
    password = PasswordField("Password", validators=[InputRequired()], render_kw={"autocomplete": "new-password", "aria-describedby": "password-errors"})

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()], render_kw={"autocomplete": "name", "aria-describedby": "username-errors"})
    password = PasswordField("Password", validators=[InputRequired()], render_kw={"autocomplete": "new-password", "aria-describedby": "password-errors"})
