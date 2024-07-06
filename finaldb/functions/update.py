import mongoengine as db
from models.department import Department
from models.course import Course
from models.student import Student

def update_department_abbreviation(old_abbreviation, new_abbreviation):
    try:
        department = Department.objects(abbreviation=old_abbreviation).first()
        if not department:
            raise ValueError('Department not found')
        department.abbreviation = new_abbreviation
        department.save()
        print(f'Department updated: {department}')
    except db.errors.NotUniqueError:
        print(f'Error: A department with the abbreviation "{new_abbreviation}" already exists.')
    except (db.ValidationError, ValueError) as e:
        print(f'Error updating department abbreviation: {e}')

def update_course_name(department_abbreviation, courseNumber, new_courseName):
    try:
        department = Department.objects(abbreviation=department_abbreviation).first()
        if not department:
            raise ValueError('Department not found')
        course = Course.objects(department=department, courseNumber=courseNumber).first()
        if not course:
            raise ValueError('Course not found')
        course.courseName = new_courseName
        course.save()
        print(f'Course updated: {course}')
    except db.errors.NotUniqueError:
        print(f'Error: A course with the name "{new_courseName}" in department "{department_abbreviation}" already exists.')
    except (db.ValidationError, ValueError) as e:
        print(f'Error updating course name: {e}')

def update_student_name(email, new_lastName, new_firstName):
    try:
        student = Student.objects(email=email).first()
        if not student:
            raise ValueError('Student not found')
        student.lastName = new_lastName
        student.firstName = new_firstName
        student.save()
        print(f'Student updated: {student}')
    except (db.ValidationError, ValueError) as e:
        print(f'Error updating student name: {e}')