import csv
import random
import pandas as pd
import datetime
import itertools

DEPT = dict()
MAJOR = dict()
STUDENT_ID = list()
FACULTY_ID = list()

def get_all_students():
    student_data = read_csv_file('./statics/data/students.csv')
    return list(zip(*student_data))[0]

def get_all_faculity():
    fac_data = read_csv_file('./statics/data/faculty.csv')
    return list(zip(*fac_data))[0]

def get_all_majors():
    major_data = read_csv_file('./statics/data/major.csv')
    return list(zip(*major_data))[0]

def get_all_courses():
    course_data = read_csv_file('./statics/data/courses.csv')
    return list(zip(*course_data))[0]

def get_all_semester():
    sem_data = read_csv_file('./statics/data/semesters.csv')
    return list(zip(*sem_data))[0]

def generate_semester_csv():
    datelist = pd.date_range(start='1/01/1950', end='1/10/2021', freq='4M').tolist()
    with open('./statics/data/semesters.csv', 'w+') as f:
        for i in range(0, len(datelist)-1):
            exam_sdate = datelist[i+1] - pd.Timedelta(days=14)
            exam_edate = datelist[i+1] - pd.Timedelta(days=7)
            drop_date = datelist[i] + pd.Timedelta(days=7)
            end_date = exam_edate + pd.Timedelta(days=1)

            writer = csv.writer(f, delimiter=',')
            writer.writerow(['SEM'+str(i), datelist[i].date(),
                             end_date.date(),
                             exam_sdate.date(),
                             exam_edate.date(),
                             drop_date.date()])

def read_csv_file(name):
    with open(name, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        return list(data)

def generate_section_sql():
    sem_data = get_all_semester()
    courses = list(get_all_courses())
    section_id = list(itertools.chain(*read_csv_file('./statics/data/sections.csv')))
    for sec in section_id:
        pass


def generate_prereq_sql():
    courses = list(get_all_courses())
    num_adv_courses = int(len(courses) * .25)
    adv_courses = random.sample(courses, num_adv_courses)
    for c in adv_courses:
        courses.remove(c)

    template = "insert into prereq (course_num, pcourse_num) values " \
               "('%s', '%s');\n"
    with open("./statics/sql/prereq.sql", 'w+') as f:
        for c in adv_courses:
            num_prereqs = random.randint(1, 4)
            prereqs = random.sample(courses, num_prereqs)
            for prereq in prereqs:
                sql = template % (c, prereq)
                f.write(sql)

def generate_students_major_sql():
    students = list(get_all_students())
    majors = list(get_all_majors())
    template = "insert into student_major (stu_num,major_num) values " \
               "(%d, %d);\n"
    with open('./statics/sql/studentmajors.sql', 'w+') as f:
        for student in students:
            achievement = random.randint(0, 10)
            num_majors = len(majors)
            if achievement <= 1:
                for i in range(0, 3):
                    ind = random.randint(0, num_majors-1)
                    sql = template % (int(student), int(majors[ind]))
                    f.write(sql)
            elif achievement > 6:
                for i in range(0, 2):
                    ind = random.randint(0, num_majors-1)
                    sql = template % (int(student), int(majors[ind]))
                    f.write(sql)
            else:
                ind = random.randint(0, num_majors-1)
                sql = template % (int(student), int(majors[ind]))
                f.write(sql)

def generate_advises_sql():
    students = list(get_all_students())
    fac = list(get_all_faculity())
    template = "insert into advises (stu_dent,fac,num) values " \
               "(%d, %d);\n"
    with open('./statics/sql/advises.sql', 'w+') as f:
        for data in fac:
            does_advise = random.randint(0,10)
            if does_advise > 5:
                num_advise = random.randint(1,10)
                number_students = len(students)
                index = random.sample(range(number_students), num_advise)
                rm = []
                for stu_index in index:
                    sql = template % (int(data), int(students[stu_index]))
                    f.write(sql)
                    rm.append(students[stu_index])
                for stu in rm:
                    students.remove(stu)

def generate_students_sql():
    student_data = read_csv_file('./statics/data/students.csv')
    template = "insert into student (stu_num,last_name,first_name,address," \
               "city,credits_earned, gpa,class_standing) values " \
               "(%d,'%s','%s','%s','%s',%d,%.2f,'%s');\n"
    with open('./statics/sql/students.sql','w+') as f:
        for data in student_data:
            if float(data[6]) > 2.0:
                standing = "Good Standing"
            elif float(data[6]) > 1.0:
                standing = "Probabtion"
            else:
                standing = "Failing"
            sql = template % (int(data[0]), data[1].replace("'", ""),
                              data[2].replace("'", ""), data[3], data[4],
                              float(data[5]), float(data[6]), standing)
            f.write(sql)

def generate_courses_sql():
    course_data = read_csv_file('./statics/data/courses.csv')
    template = "insert into course (course_num,dept_code,title,credits) values " \
               "('%s','%s','%s',%d);\n"
    with open('./statics/sql/courses.sql', 'w+') as f:
        for data in course_data:
            sql = template % (data[0], DEPT[random.choice(list(DEPT.keys()))], data[1], int(data[2]))
            f.write(sql)

def generate_semester_sql():
    generate_semester_csv()
    sem_data = read_csv_file('./statics/data/semesters.csv')
    template = "insert into semester (seme_code,start_date,end_date," \
               "exam_sdate,exam_edate,withdrawal_date) values " \
               "('%s','%s','%s','%s','%s','%s');\n"
    with open('./statics/sql/semester.sql', 'w+') as f:
        for data in sem_data:
            sql = template % (data[0], data[1], data[2], data[3], data[4], data[5])
            f.write(sql)

def generate_majors_sql():
    major_data = read_csv_file('./statics/data/major.csv')
    template = "insert into major (major_num,description,dept_code) " \
               "values (%d,'%s','%s');\n"
    with open('./statics/sql/major.sql', 'w+') as f:
        for data in major_data:
            sql = template % (int(data[0]), data[1], data[2])
            f.write(sql)

def generate_office_sql():
    office_data = read_csv_file('./statics/data/faculty.csv')
    template = "insert into office (office_num,phone) " \
               "values (%d,'%s');\n"
    with open("./statics/sql/office.sql", 'w+') as f:
        for data in office_data:
            sql = template % (int(data[6]),data[7])
            f.write(sql)

def generate_faculty_sql():
    faculty_data = read_csv_file('./statics/data/faculty.csv')
    template = "insert into faculty (fac_num,last_name,first_name,address,city,start_date,office_num,dept_code) " \
               " values (%d,'%s','%s','%s','%s','%s',%d,'%s');\n"
    with open('./statics/sql/faculty.sql', 'w+') as f:
        for data in faculty_data:
            dept_num = random.choice(list(DEPT.keys()))
            sql = template % (int(data[0]), data[1], data[2], data[3], data[4], data[5],int(data[6]),dept_num)
            f.write(sql)

def generate_department_sql():
    dept_data = read_csv_file('./statics/data/department.csv')
    template = "insert into department (dept_code, dept_name, location)" \
               " values ('%s', '%s', '%s');\n"
    with open('./statics/sql/department.sql', 'w+') as f:
        for data in dept_data:
            dept_code = data[0]
            dept_name = data[1]
            location = data[2]
            DEPT[dept_name] = dept_code
            sql = template % (dept_code, dept_name, location)
            f.write(sql)

if __name__ == '__main__':
    #generate_department_sql()
    #generate_majors_sql()

    #generate_office_sql()

    #generate_faculty_sql()
    #generate_courses_sql()
    #generate_students_sql()

    #generate_advises_sql()
    #generate_students_major_sql()
    #generate_prereq_sql()
    generate_section_sql()