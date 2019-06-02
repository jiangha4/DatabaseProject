from flask import Flask, Blueprint
from api.restplus import api
from api.endpoints.routes import ns
import settings

app = Flask(__name__)

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
    flask_app.register_blueprint(blueprint)

def main():
    init_app(app)
    #log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)

if __name__ == '__main__':
    main()