from flask import Blueprint
from flask import jsonify

from config import settings
from src.blueprints.main.decorator import exponential_backoff


bp = Blueprint("main", __name__, url_prefix="/api")


@bp.route("/")
# @exponential_backoff(retries=3)
def simulated_process():
    # To simulate a faulty/overloaded service
    circuit_breaker = settings.CIRCUIT_BREAKER_FLAG
    
    