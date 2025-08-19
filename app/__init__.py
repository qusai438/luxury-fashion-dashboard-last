from flask import Flask
from .routes import bp as core_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(core_bp)
    return app
