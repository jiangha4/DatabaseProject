from .. import restplus
from .. import parser
from .. import serializer
from flask_restplus import Resource
import csv

from statics.models.database import myDB

ns = restplus.api.namespace('SimpleQueries',
                            description='These are simple queries that a school'
                                        'administrator would want to see')
ns2 = restplus.api.namespace('StoredProcedure')



@ns.route('/studentinfo')
class AllStudentCollection(Resource):
    #@restplus.api.marshal_with(serializer.studentinfo)
    def get(self):
        return None


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


@ns2.route('/hello')
class StoreCollection(Resource):
    @restplus.api.expect(parser.args, validate=True)
    def get(self):
        return None