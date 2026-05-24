from flask import Blueprint

input_bp = Blueprint("input", __name__)


@input_bp.route("/")
def get_input():
    return "<h1>Your input is here</h1>"
