from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    app.debug = app.config["DEBUG"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DATABASE_URI"]

    db.init_app(app)


    from .views import padds
    app.register_blueprint(padds)

    return app

