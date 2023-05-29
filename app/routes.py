from flask import redirect, request, render_template, url_for
from app import app
from app.forms import LoginForm, RegistrationForm

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
        # TODO:
        return
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST" and form.validate():
        return redirect(url_for("dashboard"))
    return render_template("register.html", form=form)