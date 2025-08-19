from flask import Blueprint, jsonify

bp = Blueprint("core", __name__)

@bp.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@bp.route("/version")
def version():
    return jsonify({"version": "1.0.0"}), 200
