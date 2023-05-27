from flask import redirect, request, render_template, url_for
from app import app
from app.forms import LoginForm, RegistrationForm
from app.utils import is_valid_user, create_user

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
        if is_valid_user(form.username.data):
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