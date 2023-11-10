from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')

    from .routes import main
    app.register_blueprint(main)

    return app
