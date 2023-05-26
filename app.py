from flask import Flask, redirect, request, render_template, url_for, session
from forms import LoginForm, RegistrationForm
import bcrypt

app = Flask(__name__)
app.secret_key = 'my secret key'.encode('UTF-8')

# Protect against CSRF
app.config["SESSION_COOKIE_SAMESITE"] = "Strict"
# Protect against XSS user hijacking
app.config["SESSION_COOKIE_HTTPONLY"] = True
# Only send if HTTPS
app.config["SESSION_COOKIE_SECURE"] = True

# Mock users table, in lieu of a DB. Obviously not acceptable for production but useful for demo purposes.
users = {}

@app.route("/", methods=["GET"])
def index():
    # TODO: if user is logged in
    if False:
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/dashboard", methods=["GET"])
def dashboard():
    # TODO: If user is logged in
    if True:
        return render_template("dashboard.html")
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        # Check if user exists
        # TODO: actually log in, though. Set cookie.
        if form.username.data in users:
            return redirect(url_for("dashboard"))
        # TODO: tell them that this user does not exist... custom validator?
        return redirect(url_for("login"))
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST" and form.validate():
        create_user(form)
        return redirect(url_for("dashboard"))
    return render_template("register.html", form=form)

def create_user(form):
    username = form.username.data
    password = form.password.data
    # In reality, this would be a DB call
    if (username in users):
        # TODO: this should be done at the form validation step...
        return (f"{username} already exists", 409)
    # Salt and hash the password
    password_encoded = password.encode("UTF-8")
    password_salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(password_encoded, password_salt)
    # Mock DB persistence
    users[username] = {
        "password": password_hashed,
    }
    return users[username]

if __name__ == "__main__":
    # See devcert.sh
    context = ('certificate.pem', 'privatekey.pem')
    app.run(debug=True, ssl_context=context, host="127.0.0.1", port=5000)