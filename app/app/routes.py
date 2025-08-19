import os
from flask import Blueprint, jsonify, Response

bp = Blueprint("core", __name__)

@bp.get("/health")
def health():
    return jsonify({"ok": True}), 200

@bp.get("/version")
def version():
    env = os.getenv("APP_ENV", "staging")
    return jsonify({"name": "LuxuryDashboard", "env": env}), 200

@bp.get("/")
def home():
    return Response(
        "<h1>Dashboard Running ✅</h1><p><a href='/health'>/health</a> • <a href='/version'>/version</a></p>",
        mimetype="text/html"
    )
