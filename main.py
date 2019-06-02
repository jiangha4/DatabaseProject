from statics.models.database import myDB
from flask import Flask
from flask_restplus import Resource, Api


USERNAME = "s19wdb37"
PASSWORD = "j8+k3Xqmmn"
DATABASE = "s19wdb37"
HOSTNAME = "dbclass.cs.pdx.edu"

def main():
    #myDB = myDB(USERNAME, PASSWORD, DATABASE, HOSTNAME)

    app = Flask(__name__)  # Create a Flask WSGI application
    api = Api(app)  # Create a Flask-RESTPlus API

    @api.route('/hello')  # Create a URL route to this resource
    class HelloWorld(Resource):  # Create a RESTful resource
        def get(self):  # Create GET endpoint
            return {'hello': 'world'}

    if __name__ == '__main__':
        app.run(debug=True)  # Start a development server

if __name__ == '__main__':
    main()