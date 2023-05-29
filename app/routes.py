from flask import redirect, request, render_template, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from app import app, database
from app.forms import LoginForm, RegistrationForm
from app.models import User

@app.route("/", methods=["GET"])
def index():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@app.route("/login", methods=["GET", "POST"])
def login():
    # Already logged in
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form = LoginForm(request.form)
    # POST = form submission. GET = normal view.
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("dashboard"))
    # Normal GET or POST with errors
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form = RegistrationForm()
    # POST = form submission. GET = normal view.
    if request.method == "POST" and form.validate():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        database.session.add(user)
        database.session.commit()
        login_user(user)
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("dashboard"))
    # Normal GET or POST with errors
    return render_template("register.html", form=form)

@app.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("index"))