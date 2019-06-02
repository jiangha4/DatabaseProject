CREATE table Student (
stu_num        INT PRIMARY KEY, 
last_name      VARCHAR(15),
first_name     VARCHAR(15),
address        VARCHAR(40),
city           VARCHAR(20),
credits_earned NUMERIC,
gpa            NUMERIC(3,2),
class_standing VARCHAR(15));  

CREATE table Faculty (
fac_num        INT PRIMARY KEY,
last_name      VARCHAR(15),
first_name     VARCHAR(15),
address        VARCHAR(40),
city           VARCHAR(20),
current_rank   VARCHAR(20),
start_date     DATE,
office_num     INT,
dept_code      VARCHAR(6));

CREATE table Office (
office_num     INT PRIMARY KEY,
phone          VARCHAR(10));

CREATE table Department (
dept_code      VARCHAR(6) PRIMARY KEY,
dept_name      VARCHAR(20),
location       VARCHAR(20));

CREATE table Major (
major_num      INT PRIMARY KEY,
description    VARCHAR(40),
dept_code      VARCHAR(6));

CREATE table Advises (
stu_num        INT,
fac_num        INT);

CREATE table Semester (
seme_code      VARCHAR(6) PRIMARY KEY,
start_date     DATE,
end_date       DATE,
exam_sdate     DATE,
exam_edate     DATE,
withdrawal_date  DATE);

CREATE table Course (
course_num     VARCHAR(6) PRIMARY KEY,
dept_code      VARCHAR(6),
title          VARCHAR(25),
credits        NUMERIC);

CREATE table Section (
sect_code      INT,
seme_code      VARCHAR(6),
course_num     VARCHAR(6),
time           VARCHAR(40),
room           VARCHAR(8),
curr_enrollment INT,
max_enrollment  INT,
fac_num         INT);

CREATE table StudentGrade (
sect_code      INT,
seme_code      VARCHAR(6),
course_num     VARCHAR(6),
stu_num        INT, 
grade          VARCHAR(2),
credits_earned  NUMERIC,
grade_points    NUMERIC(4,2));

CREATE TABLE PreReq (
course_num     VARCHAR(6),
pcourse_num    VARCHAR(6));

CREATE TABLE StudentMajor (
stu_num        INT,
major_num      INT);

ALTER TABLE Major
ADD FOREIGN KEY(dept_code)
REFERENCES Department(dept_code);

ALTER TABLE Advises
ADD FOREIGN KEY(fac_num)
REFERENCES Faculty(fac_num);

ALTER TABLE Advises
ADD FOREIGN KEY(stu_num)
REFERENCES Student(stu_num);

ALTER TABLE Advises
ADD PRIMARY KEY (stu_num, fac_num);

ALTER TABLE Faculty
ADD FOREIGN KEY (office_num)
REFERENCES Office (office_num);

ALTER TABLE Faculty
ADD FOREIGN KEY (dept_code)
REFERENCES Department(dept_code);

ALTER TABLE Course
ADD FOREIGN KEY (dept_code)
REFERENCES Department(dept_code);

ALTER TABLE Section
ADD FOREIGN KEY (seme_code)
REFERENCES Semester(seme_code);

ALTER TABLE Section
ADD FOREIGN KEY (fac_num)
REFERENCES Faculty(fac_num);

ALTER TABLE Section
ADD FOREIGN KEY (course_num)
REFERENCES Course(course_num);

ALTER TABLE Section
ADD PRIMARY KEY (sect_code, seme_code, course_num);

ALTER TABLE StudentGrade
ADD FOREIGN KEY (sect_code, seme_code, course_num)
REFERENCES Section(sect_code, seme_code, course_num);

ALTER TABLE StudentGrade
ADD FOREIGN KEY (stu_num)
REFERENCES Student(stu_num);

ALTER TABLE StudentGrade
ADD PRIMARY KEY (sect_code, seme_code, course_num, stu_num);

ALTER TABLE Prereq
ADD FOREIGN KEY (course_num) 
REFERENCES Course(course_num);

ALTER TABLE Prereq
ADD FOREIGN KEY (pcourse_num)
REFERENCES Course(course_num);

ALTER TABLE Prereq
ADD PRIMARY KEY (course_num, pcourse_num);

ALTER TABLE StudentMajor
ADD FOREIGN KEY (stu_num) 
REFERENCES Student(stu_num);

ALTER TABLE StudentMajor
ADD FOREIGN KEY (major_num) 
REFERENCES Major(major_num);

ALTER TABLE StudentMajor
ADD PRIMARY KEY (stu_num, major_num);

