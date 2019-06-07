from flask_restplus import fields
from api import restplus

studentinfo = restplus.api.model('Student Record', {
    'Student Number': fields.Integer(attribute='stu_num'),
    'First Name': fields.String(attribute='first_name'),
    'Last Name': fields.String(attribute='last_name'),
    'Address': fields.String(attribute='address'),
    'City': fields.String(attribute='city'),
    'Credits': fields.Integer(attribute='credits_earned'),
    'GPA': fields.Float(attribute='gpa'),
    'Standing': fields.String(attribute='class_standing')
})

departmentinfo = restplus.api.model('Department Info', {
    'Department Code': fields.Integer(attribute='dept_code'),
    'Department Name': fields.String(attribute='dept_name'),
    'Location': fields.String(attribute='location')
})

facultyinfo = restplus.api.model('Faculty Record', {
    'Faculty Number': fields.Integer(attribute='fac_num'),
    'First Name': fields.String(attribute='first_name'),
    'Last Name': fields.String(attribute='last_name'),
    'Address': fields.String(attribute='address'),
    'City': fields.String(attribute='city'),
    'Start Date': fields.DateTime(attribute='start_date'),
    'Office Number': fields.Integer(attribute='office_num'),
    'Department Code': fields.Integer(attribute='dept_code')
})

hiredinfo = restplus.api.model('Hire Date', {
    'Faculty Number': fields.Integer(attribute='fac_num'),
    'First Name': fields.String(attribute='first_name'),
    'Last Name': fields.String(attribute='last_name'),
    'Start Date': fields.DateTime(attribute='start_date')
})

majorinfo = restplus.api.model('Major Data',{
    'Code': fields.Integer(attribute='major_num'),
    'Name': fields.String(attribute='description')
})

majordeptinfo = restplus.api.model('Major in Dept', {
    'Code': fields.Integer(attribute='major_num'),
    'Major Name': fields.String(attribute='description'),
})

studentmajorinfo = restplus.api.model('Students and Majors', {
    'Student Number': fields.Integer(attribute='stu_num'),
    'First Name': fields.String(attribute='student.first_name'),
    'Last Name': fields.String(attribute='student.last_name'),
    'Major': fields.String(attribute='major.description')
})

courseinfo = restplus.api.model('Courses', {
    'Course Number': fields.String(attribute='course_num'),
    'Course Name': fields.String(attribute='title'),
    'Credits': fields.Integer(attribute='credits')
})

studentpermajor = restplus.api.model('Student Per Major', {
    'Major': fields.String(attribute='description'),
    'Number of Students': fields.String(attribute='num_students')
})

advisorperstudent = restplus.api.model('Number of students per Advisor', {
    'Faculty Number': fields.Integer(attribute='teacher.fac_num')
})

section = restplus.api.model('Section info', {
    'Name': fields.String(attribute='course_num'),
    'Enrollment': fields.Integer(attribute='curr_enrollment')
})

waitlist = restplus.api.model('Waitlist info', {
    'Name': fields.String(attribute='course_num'),
    'Waitlist': fields.Integer(attribute='wait_list')
})