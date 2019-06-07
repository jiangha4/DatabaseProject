from api import restplus
from api import parser
from api import serializer
from flask_restplus import Resource
from datetime import datetime, timedelta
from sqlalchemy import func
import psycopg2 as p

ns = restplus.api.namespace('Queries',
                            description='These are simple queries that a school'
                                        ' administrator would want to see')
ns_input = restplus.api.namespace('UserInput',
                                  description='Queries that require user input')

ns_stored = restplus.api.namespace('StoreProcedure',
                                   desciption="Executes a stored procedure")

from statics.models.datamodels import Student
from statics.models.datamodels import Department
from statics.models.datamodels import Faculty
from statics.models.datamodels import Major
from statics.models.datamodels import Advises
from statics.models.datamodels import Section
from statics.models.datamodels import Course
from statics.models.datamodels import StudentMajor

from app import db

@ns.route('/num_of_students')
class NumOfStudents(Resource):
    def get(self):
        r = Student.query.count()
        return {'Number': r}

@ns.route('/num_of_faculty')
class NumOfFaculty(Resource):
    def get(self):
        r = Faculty.query.count()
        return {'Number': r}

@ns.route('/student_info')
class AllStudentCollection(Resource):
    @restplus.api.marshal_with(serializer.studentinfo)
    def get(self):
        students = Student.query.all()
        return students

@ns.route('/courses')
class AllCoursesCollection(Resource):
    @restplus.api.marshal_with(serializer.courseinfo)
    def get(self):
        r = Course.query.all()
        return r

@ns.route('/department_info')
class AllDepartmentCollection(Resource):
    @restplus.api.marshal_with(serializer.departmentinfo)
    def get(self):
        departments = Department.query.all()
        return departments

@ns.route('/faculty_info')
class AllFacultyCollection(Resource):
    @restplus.api.marshal_with(serializer.facultyinfo)
    def get(self):
        facultys = Faculty.query.all()
        return facultys

@ns.route('/faculty_hire_date')
class HireDateCollection(Resource):
    @restplus.api.marshal_with(serializer.hiredinfo)
    def get(self):
        past = datetime.now() - timedelta(weeks=260)
        r = Faculty.query.filter(Faculty.start_date>past).all()
        return r

@ns.route('/majors')
class AllMajorCollection(Resource):
    @restplus.api.marshal_with(serializer.majorinfo)
    def get(self):
        r = Major.query.all()
        return r

@ns.route('/students_and_major')
class AllStudentMajorCollection(Resource):
    @restplus.api.marshal_with(serializer.studentmajorinfo)
    def get(self):
        r = StudentMajor.query.join(Major, Major.major_num == StudentMajor.major_num
                            ).join(Student, Student.stu_num == StudentMajor.stu_num
                            ).all()
        return r

@ns.route('/num_of_students_per_major')
class StudentPerMajorCollection(Resource):
    def get(self):
        r = Major.query.join(StudentMajor, StudentMajor.major_num == Major.major_num
                ).with_entities(Major.description, func.count(StudentMajor.stu_num).label('num_students')
                                ).group_by(Major.description).all()
        return r

@ns.route('/students_without_advisors')
class StudentNoAdvisorCollection(Resource):
    def get(self):
        r = Student.query.join(Advises, Advises.stu_num == Student.stu_num).count()
        num_students = Student.query.count()
        return num_students - r

@ns.route('/num_students_advisor')
class NumStudentAdvisorCollection(Resource):
    #@restplus.api.marshal_with(serializer.advisorperstudent)
    def get(self):
        r = Advises.query.join(Faculty, Faculty.fac_num == Advises.fac_num
                               ).with_entities(Advises.fac_num,
                                               Faculty.first_name,
                                               Faculty.last_name,
                                               func.count(Advises.stu_num).label('num_students')
                                               ).group_by(Advises.fac_num,
                                                          Faculty.first_name,
                                                          Faculty.last_name).all()
        return r

@ns.route('/getMVP')
class MVPTeacherCollection(Resource):
    def get(self):
        pass

@ns.route('/get_courses_for semester')
class CoursesPerSemesterCollection(Resource):
    @restplus.api.marshal_with(serializer.section)
    def get(self):
        r = Section.query.filter(Section.seme_code == 'SEM0').all()
        return r

@ns.route('/courses_waitlists')
class CoursesWithWaitlistsCollection(Resource):
    @restplus.api.marshal_with(serializer.waitlist)
    def get(self):
        r = Section.query.filter(Section.wait_list > 0
                        ).filter(Section.seme_code == 'SEM3').all()
        return r

@ns_input.route('/add_student')
class AddStudentCollection(Resource):
    @restplus.api.expect(parser.student_args, validate=True)
    def put(self):
        standing = "Error"
        args = parser.student_args.parse_args()
        if args['gpa'] > 2.0:
            standing = "Good Standing"
        elif args['gpa'] > 1.0:
            standing = "Probabtion"
        else:
            standing = "Failing"
        new_student = Student(args['stu_num'],
                              args['last_name'],
                              args['first_name'],
                              args['address'],
                              args['city'],
                              args['credits'],
                              args['gpa'],
                              standing)
        db.session.add(new_student)
        db.session.commit()

        return "Success. Inserted row!"

@ns_input.route('/get_all_majors_by_dept')
class MajorsByDeptCollection(Resource):
    @restplus.api.expect(parser.dept_args, validate=True)
    @restplus.api.marshal_with(serializer.majordeptinfo)
    def get(self):
        args = parser.dept_args.parse_args()
        r = Major.query.join(Department, Department.dept_code == Major.dept_code
                               ).filter(Department.dept_name == args['dept_num']).all()

        return r

@ns_input.route('/get_info_student')
class SpecificStudentCollection(Resource):
        @restplus.api.expect(parser.specific_student, validate=True)
        @restplus.api.marshal_with(serializer.studentinfo)
        def get(self):
            args = parser.specific_student.parse_args()
            if args['stu_num_manual']:
                target = args['stu_num_manual']
            else:
                target = int(args['stu_num'])

            r = Student.query.filter(Student.stu_num == target).all()
            return r

@ns_stored.route('/get_faculty')
class SpecificFacultyCollection(Resource):
    @restplus.api.expect(parser.specific_faculty, validate=True)
    def get(self):
        args = parser.specific_faculty.parse_args()
        conn = p.connect('postgresql://localhost/project3')
        cur = conn.cursor()
        query = "SELECT * FROM get_faculty_by_num(%d)" % args['fac_num']
        cur.execute(query)
        row = cur.fetchone()
        return {'Faculty Number': row[0], "First Name": row[1], "Last Name": row[2]}