from flask_sqlalchemy import SQLAlchemy

# type: ignore
db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    return db
