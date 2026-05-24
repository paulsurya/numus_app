from flask import Blueprint
from flask.templating import render_template

dashBoard_bp = Blueprint("dashBoard", __name__)


@dashBoard_bp.route("/")
def dashboard():
    return render_template("dashboard.html")
