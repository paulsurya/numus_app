from flask import Blueprint

dashBoard_bp = Blueprint("dashBoard", __name__)


@dashBoard_bp.route("/")
def dashBoard():
    return "<h>Hello, Hi!</h>"
