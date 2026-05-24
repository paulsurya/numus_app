from flask import Blueprint, render_template

input_bp = Blueprint("input", __name__)


@input_bp.route("/")
def get_input():
    return render_template("input.html")
