from flask import Blueprint
from flask.templating import render_template

dashBoard_bp = Blueprint("dashBoard", __name__)


@dashBoard_bp.route("/")
def dashBoard():
    return render_template("input.html")
