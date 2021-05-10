from flask import Blueprint
from flask import jsonify

from config import settings


bp = Blueprint("main", __name__, url_prefix="/api")


@bp.route("/")
def simulated_process():
    # To simulate a faulty/overloaded service
    circuit_breaker = settings.CIRCUIT_BREAKER_FLAG

    from src.blueprints.main.tasks import simulated_task
    simulated_task.delay(circuit_breaker, retries=3)

    return jsonify({"status": "ok", "message": "Task scheduled"})
