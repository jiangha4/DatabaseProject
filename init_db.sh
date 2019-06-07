#!/bin/sh/bash

init_db(){
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
}

populate_db(){
    USERNAME=davidjiang
    DATABASE=project4

    psql -U $USERNAME -d $DATABASE -a -f statics/sql/students.sql
    psql -U $USERNAME -d $DATABASE -a -f statics/sql/department.sql
    psql -U $USERNAME -d $DATABASE -a -f statics/sql/office.sql
    psql -U $USERNAME -d $DATABASE -a -f statics/sql/faculty.sql
    psql -U $USERNAME -d $DATABASE -a -f statics/sql/major.sql
    psql -U $USERNAME -d $DATABASE -a -f statics/sql/studentmajors.sql
    psql -U $USERNAME -d $DATABASE -a -f statics/sql/courses.sql
    psql -U $USERNAME -d $DATABASE -a -f statics/sql/prereq.sql
    psql -U $USERNAME -d $DATABASE -a -f statics/sql/advises.sql
    psql -U $USERNAME -d $DATABASE -a -f statics/sql/semester.sql
    psql -U $USERNAME -d $DATABASE -a -f statics/sql/section.sql
    psql -U $USERNAME -d $DATABASE -a -f statics/sql/storedproc.sql
}

upgrade_db(){
    python manage.py db migrate
    python manage.py db upgrade
}

init_db
populate_db
#upgrade_db

