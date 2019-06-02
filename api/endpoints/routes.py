from .. import restplus
from .. import parser
from flask_restplus import Resource

ns = restplus.api.namespace('Queries', description='')
ns2 = restplus.api.namespace('Stored Procedure')

@ns.route('/hello')
class BenchmarkCollection(Resource):
    @restplus.api.expect(parser.args, validate=True)
    #@restplus.api.marshal_with(serializer.response)
    def get(self):
        """
            Get benchmark metrics
        """
        args = parser.args.parse_args()
        company = args['company']
        metric = args['metric']

        #return metrics.response_object(company, metric)

@ns.route('/database')
class QueryCollection(Resource):
    @restplus.api.expect(parser.args, validate=True)
    def get(self):
        return None

@ns2.route('/hello')
class StoreCollection(Resource):
    @restplus.api.expect(parser.args, validate=True)
    def get(self):
        return None