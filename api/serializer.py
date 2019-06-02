from flask_restplus import fields
from . import restplus

studentinfo = restplus.api.model('Query Reponse', {
    'Student Number': fields.String(attribute='stu_id'),
    'First Name': fields.String(attribute='first_name'),
    'Last Name': fields.String(attirbute='last_name'),
    'Address': fields.String(attribute='address'),
    'City': fields.String(attribute='city')
})

