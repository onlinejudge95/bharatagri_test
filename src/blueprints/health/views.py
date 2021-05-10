from flask import Blueprint
from flask import jsonify


bp = Blueprint("health", __name__)


@bp.route("/health")
def health_check():
    return jsonify({"status": "ok"})
