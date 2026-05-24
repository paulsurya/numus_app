from flask import Flask

from .views.auth import auth_bp

app = Flask(__name__)


def create_app():

    app.register_blueprint(auth_bp, url_prefix="/")

    return app
