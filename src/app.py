from flask import Flask

from src.blueprints.health import health_bp
from src.blueprints.main import main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings")

    app.register_blueprint(health_bp)
    app.register_blueprint(main_bp)

    return app
