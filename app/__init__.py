from flask import Flask
from config import Config
from app.database.connection import Database
from app.routes.contactos import contactos_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Database.init_db()
    app.register_blueprint(contactos_bp)

    return app
