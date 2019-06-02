from flask_restplus import reqparse

# Contains the arguments for the query
args = reqparse.RequestParser()
args.add_argument('company', type=str, required=True)
                   #choices=get_all_companies())
args.add_argument('metric', type=str, required=True)
                  #choices=csv_file._valid_csv_fields)