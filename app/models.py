from app import database, login
from bcrypt import gensalt, hashpw, checkpw
from flask_login import UserMixin

# All that UserMixin does is add some methods: https://github.com/maxcountryman/flask-login/blob/b30758205211c3af4ac6a41601aee17f6aa45f64/src/flask_login/mixins.py#L11C1-L27
class User(UserMixin, database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(64), index=True, unique=True)
    password_hash = database.Column(database.String(128))

    def set_password(self, password):
        password_encoded = password.encode("UTF-8")
        password_salt = gensalt()
        password_hash = hashpw(password_encoded, password_salt)
        self.password_hash = password_hash

    def check_password(self, password):
        return checkpw(password, self.password_hash)

    def __repr__(self):
        return '<User {}>'.format(self.username)

# Since flask_login is database-independent, we need to tell it how to find a particular user by ID
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
