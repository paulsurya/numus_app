from crypt import methods

from flask import Blueprint, redirect, render_template

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST", "GET"])
def login():

    if methods == "POST":
        redirect("/")

    return render_template("login.html")
