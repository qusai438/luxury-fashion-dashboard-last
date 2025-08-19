from flask import Flask, jsonify
import os

def create_app():
    app = Flask(__name__)

    # Basic config
    app.config["APP_ENV"] = os.getenv("APP_ENV", "development")

    # Core routes
    @app.route("/health")
    def health():
        return jsonify({"ok": True}), 200

    @app.route("/version")
    def version():
        return jsonify({
            "name": "LuxuryFashionCore",
            "env": app.config["APP_ENV"]
        }), 200

    return app


app = create_app()
