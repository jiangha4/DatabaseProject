from app import db

class Student(db.Model):
    __tablename__ = 'student'

    stu_num = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String())
    first_name = db.Column(db.String())
    address = db.Column(db.String())
    city = db.Column(db.String())
    credits_earned = db.Column(db.Numeric)
    gpa = db.Column(db.Numeric)
    class_standing = db.Column(db.String())
    stu_majors = db.relationship('StudentMajor', backref='student', lazy=True)
    mentor = db.relationship('Advises', backref='student', lazy=True)

    def __init__(self, stu_num, last_name, first_name, address, city,
                 credits_earned, gpa, class_standing):
        self.stu_num = stu_num
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.city = city
        self.credits_earned = credits_earned
        self.gpa = gpa
        self.class_standing = class_standing

    def __repr__(self):
        return '<id {}, first {}, last {}>'.format(self.stu_num, self.first_name, self.last_name)

class Department(db.Model):
    __tablename__ = 'department'

    dept_code = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String())
    location = db.Column(db.String())
    majors = db.relationship('Major', backref='department', lazy=True)

    def __init__(self, dept_code, dept_name, location):
        self.dept_code = dept_code
        self.dept_name = dept_name
        self.location = location

    def __repr__(self):
        return '<id {}>'.format(self.dept_code)

class Faculty(db.Model):
    __tablename__ = 'faculty'

    fac_num = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String())
    first_name = db.Column(db.String())
    address = db.Column(db.String())
    city = db.Column(db.String())
    start_date = db.Column(db.DateTime)
    office_num = db.Column(db.Integer, db.ForeignKey('office.office_num'))
    dept_code = db.Column(db.Integer, db.ForeignKey('department.dept_code'),
                          nullable=False)
    teaching = db.relationship('Section', backref='faculty', lazy=True)
    mentoring = db.relationship('Advises', backref='faculty', lazy=True)

    def __init__(self, fac_num, last_name, first_name, address,
                 city, start_date, dept_code):
        self.fac_num = fac_num
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.city = city
        self.start_date = start_date
        self.dept_code = dept_code

    def __repr__(self):
        return '<id {}>'.format(self.fac_num)

class Office(db.Model):
    __tablename__ = 'office'

    office_num = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String())

    def __init__(self, phone):
        self.phone = phone

    def __repr__(self):
        return '<id {}>'.format(self.office_num)

class Major(db.Model):
    __tablename__= 'major'

    major_num = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    dept_code = db.Column(db.Integer, db.ForeignKey('department.dept_code'),
                          nullable=False)
    stu_major = db.relationship('StudentMajor', backref='major', lazy=True)

    def __init__(self, description, dept_code):
        self.description = description
        self.dept_code = dept_code

    def __repr__(self):
        return '<id {}>'.format(self.major_num)

class Advises(db.Model):
    __tablename__ = 'student_advisors'

    stu_num = db.Column(db.Integer, db.ForeignKey('student.stu_num'), primary_key=True)
    fac_num = db.Column(db.Integer, db.ForeignKey('faculty.fac_num'), primary_key=True)

    def __init__(self, stu_num, fac_num):
        self.stu_num = stu_num
        self.fac_num = fac_num

    def __repr__(self):
        return '<id {}>'.format(self.stu_num)

class Semester(db.Model):
    __tablename__ = 'semester'

    seme_code = db.Column(db.String(), primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    exam_sdate = db.Column(db.DateTime)
    exam_edate = db.Column(db.DateTime)
    withdrawal_date = db.Column(db.DateTime)

    def __init__(self, start_date, end_date, exam_sdate,
                 exam_edate, withdrawal_date):
        self.start_date = start_date
        self.end_date = end_date
        self.exam_sdate = exam_sdate
        self.exam_edate = exam_edate
        self.withdrawal_date = withdrawal_date

    def __repr__(self):
        return '<id {}>'.format(self.seme_code)

class Course(db.Model):
    __tablename__ = 'dept_course'

    course_num = db.Column(db.String(), primary_key=True)
    dept_code = db.Column(db.Integer, db.ForeignKey('department.dept_code'),
                          nullable=False)
    title = db.Column(db.String())
    credits = db.Column(db.Numeric)

    def __init__(self, dept_code, title, credits):
        self.dept_code = dept_code
        self.title = title
        self.credits = credits

    def __repr__(self):
        return '<id {}>'.format(self.course_num)

class Section(db.Model):
    __tablename__ = 'section'

    sect_code = db.Column(db.String(), primary_key=True)
    seme_code = db.Column(db.String(), db.ForeignKey('semester.seme_code'), primary_key=True)
    course_num = db.Column(db.String(), primary_key=True)
    course_time = db.Column(db.String())
    curr_enrollment = db.Column(db.Integer)
    max_enrollment = db.Column(db.Integer)
    wait_list = db.Column(db.Integer)
    fac_num = db.Column(db.Integer, db.ForeignKey('faculty.fac_num'))

    def __init__(self, seme_code, course_num, time, room,
                 curr_enrollment, max_enrollment, fac_num):
        self.seme_code = seme_code
        self.course_num = course_num
        self.time = time
        self.room = room
        self.curr_enrollment = curr_enrollment
        self.max_enrollment = max_enrollment
        self.fac_num = fac_num

    def __repr__(self):
        return '<id {}>'.format(self.sect_code)


class StudentMajor(db.Model):
    __tablename__= 'student_major'

    stu_num = db.Column(db.Integer, db.ForeignKey('student.stu_num'), primary_key=True)
    major_num = db.Column(db.Integer, db.ForeignKey('major.major_num'), primary_key=True)

    def __init__(self, stu_num, major_num):
        self.stu_num = stu_num
        self.major_num = major_num

