from flask_restplus import reqparse
import data

student_args = reqparse.RequestParser()
student_args.add_argument('stu_num', type=int, required=True)
student_args.add_argument('first_name', type=str, required=True)
student_args.add_argument('last_name', type=str, required=True)
student_args.add_argument('address', type=str, required=True)
student_args.add_argument('city', type=str, required=True)
student_args.add_argument('credits', type=int, required=True)
student_args.add_argument('gpa', type=float, required=True)

dept_args = reqparse.RequestParser()
dept_args.add_argument('dept_num', type=str, required=True,
                       choices=data.get_all_depts())

specific_student = reqparse.RequestParser()
specific_student.add_argument('stu_num_manual', type=int, required=False)
specific_student.add_argument('stu_num', type=str, required=False,
                              choices=data.get_all_students())

specific_faculty = reqparse.RequestParser()
specific_faculty.add_argument('fac_num', type=int, required=True)