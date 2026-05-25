from flask import Flask
from .extension import db,migrate
from .views.auth import auth_bp
from .views.dashboard import dashBoard_bp
from .views.input import input_bp

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config['SECRET_KEY'] = "Paulis234"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(dashBoard_bp, url_prefix="/dashboard")
    app.register_blueprint(input_bp, url_prefix="/input")

    from . import models

    with app.app_context():
        db.create_all()

    return app
