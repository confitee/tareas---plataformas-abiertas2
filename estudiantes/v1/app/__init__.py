from flask import Flask
from flask_cors import CORS

from .controllers import crud_endpoints, estudiantes_endpoints


def create_app():
    app = Flask(__name__)
    app.register_blueprint(
        estudiantes_endpoints,
        url_prefix="/estudiantes/api/v1",
    )
    app.register_blueprint(crud_endpoints)
    CORS(app, origins="*")
    return app
