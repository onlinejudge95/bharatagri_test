from celery import Celery
from flask import Flask

from src.blueprints.health import health_bp
from src.blueprints.main import main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings")

    app.register_blueprint(health_bp)
    app.register_blueprint(main_bp)

    return app


def create_celery(app=None):
    app = app or create_app()

    celery = Celery(
        app.import_name,
        broker=app.config["CELERY_BROKER_URL"],
        include=app.config["CELERY_TASK_LIST"],
    )
    celery.conf.update(app.config)

    BaseTask = celery.Task

    class ContextTask(BaseTask):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return BaseTask.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
