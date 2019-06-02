from flask_restplus import Api

api = Api(version='1.0', title='Big Brother',
                  description='A overhead view of student data. '
                              'A Database project')

@api.errorhandler
def default_error_handler(e):
        message = 'An unhandled exception occurred.'
        return {'message': message}, 500