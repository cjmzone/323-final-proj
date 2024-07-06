import mongoengine as db
from models.department import Department
from models.course import Course
from models.major import Major
from models.student import Student
from models.section import Section
from models.enrollment import Enrollment
from models.student_major import StudentMajor
from datetime import datetime

def add_department(name, abbreviation, chairName, building, office, description):
    try:
        department = Department(name=name, abbreviation=abbreviation, chairName=chairName, building=building, office=office, description=description)
        department.save()
        print(f'Department added: {department}')
    except db.errors.NotUniqueError:
        print(f'Error: A department with the name "{name}" or abbreviation "{abbreviation}" already exists.')
    except db.ValidationError as e:
        print(f'Error adding department: {e}')

def add_course(department_abbreviation, courseNumber, courseName, units):
    try:
        department = Department.objects(abbreviation=department_abbreviation).first()
        if not department:
            raise ValueError('Department not found')
        course = Course(department=department, courseNumber=courseNumber, courseName=courseName, units=units)
        course.save()
        print(f'Course added: {course}')
    except db.errors.NotUniqueError:
        print(f'Error: A course with the name "{courseName}" or number "{courseNumber}" in department "{department_abbreviation}" already exists.')
    except (db.ValidationError, ValueError) as e:
        print(f'Error adding course: {e}')

def add_major(name):
    try:
        major = Major(name=name)
        major.save()
        print(f'Major added: {major}')
    except db.errors.NotUniqueError:
        print(f'Error: A major with the name "{name}" already exists.')
    except db.ValidationError as e:
        print(f'Error adding major: {e}')

def add_student(lastName, firstName, email):
    try:
        student = Student(lastName=lastName, firstName=firstName, email=email)
        student.save()
        print(f'Student added: {student}')
    except db.errors.NotUniqueError:
        print(f'Error: A student with the email "{email}" already exists.')
    except db.ValidationError as e:
        print(f'Error adding student: {e}')

def add_section(course_abbreviation, courseNumber, sectionNumber, semester, sectionYear, building, room, schedule, startTime, instructor):
    try:
        department = Department.objects(abbreviation=course_abbreviation).first()
        if not department:
            raise ValueError('Department not found')
        course = Course.objects(department=department, courseNumber=courseNumber).first()
        if not course:
            raise ValueError('Course not found')
        section = Section(course=course, sectionNumber=sectionNumber, semester=semester, sectionYear=sectionYear, building=building, room=room, schedule=schedule, startTime=startTime, instructor=instructor)
        section.save()
        print(f'Section added: {section}')
    except db.errors.NotUniqueError:
        print(f'Error: A section with the number "{sectionNumber}" for course "{course_abbreviation} {courseNumber}" in semester "{semester} {sectionYear}" already exists.')
    except (db.ValidationError, ValueError) as e:
        print(f'Error adding section: {e}')
        
def add_enrollment(student_email, course_abbreviation, courseNumber, sectionNumber, semester, sectionYear, category):
    try:
        student = Student.objects(email=student_email).first()
        if not student:
            raise ValueError('Student not found')
        department = Department.objects(abbreviation=course_abbreviation).first()
        if not department:
            raise ValueError('Department not found') 
        course = Course.objects(department=department, courseNumber=courseNumber).first()
        if not course:
            raise ValueError('Course not found') 
        section = Section.objects(course=course, sectionNumber=sectionNumber, semester=semester, sectionYear=sectionYear).first()
        if not section:
            raise ValueError('Section not found')
        enrollment = Enrollment(student=student, section=section, category=category)
        enrollment.save()
        print(f'Enrollment added: {enrollment}')
    except db.errors.NotUniqueError:
        print(f'Error: The student with this email "{student_email}" is already enrolled in the section "{course_abbreviation} {courseNumber} Section {sectionNumber} ({semester} {sectionYear})".')
    except (db.ValidationError, ValueError) as e:
        print(f'Error adding enrollment: {e}')

def add_student_major(student_email, major_name):
    try:
        student = Student.objects(email=student_email).first()
        major = Major.objects(name=major_name).first()
        if not student or not major:
            raise ValueError('Student or Major not found')
        student_major = StudentMajor(student=student, major=major)
        student_major.save()
        print(f'StudentMajor added: {student_major}')
    except db.errors.NotUniqueError:
        print(f'Error: The student with this "{student_email}" has already declared the major "{major_name}".')
    except (db.ValidationError, ValueError) as e:
        print(f'Error adding student major: {e}')
