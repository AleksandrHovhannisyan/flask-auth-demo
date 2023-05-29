from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, ValidationError
from wtforms.validators import InputRequired
from app.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()], render_kw={"autocomplete": "name", "aria-describedby": "username-errors"})
    password = PasswordField("Password", validators=[InputRequired()], render_kw={"autocomplete": "new-password", "aria-describedby": "password-errors"})
    remember_me = BooleanField('Remember Me')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('Username does not exist')

    def validate_password(self, password):
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            return True
        is_password_valid = user.check_password(password.data.encode('UTF-8'))
        if not is_password_valid:
            raise ValidationError('Invalid password')

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()], render_kw={"autocomplete": "name", "aria-describedby": "username-errors"})
    password = PasswordField("Password", validators=[InputRequired()], render_kw={"autocomplete": "new-password", "aria-describedby": "password-errors"})

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
    