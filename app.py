from flask import Flask, Blueprint
from api.restplus import api
import settings
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/project4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from api.endpoints.routes import ns, ns_input, ns_stored

def configure(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def init_app(flask_app):
    configure(flask_app)
    blueprint = Blueprint('/', __name__)
    api.init_app(blueprint)
    api.add_namespace(ns)
    api.add_namespace(ns_input)
    api.add_namespace(ns_stored)
    flask_app.register_blueprint(blueprint)

def create_app():
    init_app(app)
    app.run(debug=settings.FLASK_DEBUG)

if __name__ == '__main__':
    create_app()


