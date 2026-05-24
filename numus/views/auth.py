from flask import Blueprint, render_template,flash,request

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST", "GET"], strict_slashes=False)
def login():
    if request.method == "POST":
        userName = request.form.get("username")
        pass1 = request.form.get("password1")
        pass2 = request.form.get("password2")
        if pass1 != pass2:
            print("error")
        elif len(pass1) < 7:
            print("error")
    return render_template("login.html")
