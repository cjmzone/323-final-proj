import mongoengine as db
from datetime import datetime
from models.department import Department
from models.course import Course
from models.major import Major
from models.student import Student
from models.section import Section
from models.enrollment import Enrollment
from models.student_major import StudentMajor
from datetime import datetime
from menu_definitions import *
from Utilities import Utilities
# Establish connection to MongoDB
# db.connect(db='school', host='mongodb+srv://cjmzone:wireWar21$@cecs323.dp4wxsa.mongodb.net/?retryWrites=true&w=majority&appName=cecs323')

def add(db):
    """
    Present the add menu and execute the user's selection.
    :param db:  The connection to the current database.
    :return:    None
    """
    add_action: str = ''
    while add_action != add_menu.last_action():
        add_action = add_menu.menu_prompt()
        exec(add_action)

def delete(db):
    """
    Present the delete menu and execute the user's selection.
    :param db:  The connection to the current database.
    :return:    None
    """
    delete_action: str = ''
    while delete_action != delete_menu.last_action():
        delete_action = delete_menu.menu_prompt()
        exec(delete_action)

def list_objects(db):
    """
    Present the list menu and execute the user's selection.
    :param db:  The connection to the current database.
    :return:    None
    """
    list_action: str = ''
    while list_action != list_menu.last_action():
        list_action = list_menu.menu_prompt()
        exec(list_action)

def update(db):
    """
    Present the update menu and execute the user's selection.
    :param db:  The connection to the current database.
    :return:    None
    """
    update_action: str = ''
    while update_action != update_menu.last_action():
        update_action = update_menu.menu_prompt()
        exec(update_action)

def add_department():
    try:
        name = input("Enter department name: ")
        abbreviation = input("Enter department abbreviation: ")
        chairName = input("Enter chair name: ")
        building = input("Enter building: ")
        office = input("Enter office: ")
        description = input("Enter description: ")
        department = Department(name=name, abbreviation=abbreviation, chairName=chairName, building=building, office=office, description=description)
        department.save()
        print(f'Department added: {department}')
    except db.errors.NotUniqueError:
        print(f'Error: A department with the name "{name}" or abbreviation "{abbreviation}" already exists.')
    except db.ValidationError as e:
        print(f'Error adding department: {e}')

def add_course():
    try:
        department_abbreviation = input("Enter department abbreviation: ")
        courseNumber = int(input("Enter course number: "))
        courseName = input("Enter course name: ")
        units = int(input("Enter units: "))
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
# edit to be a child of department
def add_major():
    try:
        name = input("Enter major name: ")
        major = Major(name=name)
        major.save()
        print(f'Major added: {major}')
    except db.errors.NotUniqueError:
        print(f'Error: A major with the name "{name}" already exists.')
    except db.ValidationError as e:
        print(f'Error adding major: {e}')

def add_student():
    try:
        lastName = input("Enter last name: ")
        firstName = input("Enter first name: ")
        email = input("Enter email: ")
        student = Student(lastName=lastName, firstName=firstName, email=email)
        student.save()
        print(f'Student added: {student}')
    except db.errors.NotUniqueError:
        print(f'Error: A student with the email "{email}" already exists.')
    except db.ValidationError as e:
        print(f'Error adding student: {e}')
# edit datetime
def add_section():
    try:
        department_abbreviation = input("Enter department abbreviation: ")
        courseNumber = int(input("Enter course number: "))
        sectionNumber = int(input("Enter section number: "))
        semester = input("Enter semester: ")
        sectionYear = int(input("Enter section year: "))
        building = input("Enter building: ")
        room = int(input("Enter room: "))
        schedule = input("Enter schedule: ")
        startTime = datetime.strptime(input("Enter start time (08:01): "), '%H:%M')
        instructor = input("Enter instructor: ")
        department = Department.objects(abbreviation=department_abbreviation).first()
        if not department:
            raise ValueError('Department not found')
        course = Course.objects(department=department, courseNumber=courseNumber).first()
        if not course:
            raise ValueError('Course not found')
        section = Section(course=course, sectionNumber=sectionNumber, semester=semester, sectionYear=sectionYear, building=building, room=room, schedule=schedule, startTime=startTime, instructor=instructor)
        section.save()
        print(f'Section added: {section}')
    except db.errors.NotUniqueError:
        print(f'Error: A section with the number "{sectionNumber}" for course "{department_abbreviation} {courseNumber}" in semester "{semester} {sectionYear}" already exists.')
    except (db.ValidationError, ValueError) as e:
        print(f'Error adding section: {e}')
        
def add_enrollment():
    try:
        student_email = input("Enter student email: ")
        department_abbreviation = input("Enter department abbreviation: ")
        courseNumber = int(input("Enter course number: "))
        sectionNumber = int(input("Enter section number: "))
        semester = input("Enter semester: ")
        sectionYear = int(input("Enter section year: "))
        category = input("Enter category (PassFail/LetterGrade): ")
        student = Student.objects(email=student_email).first()
        if not student:
            raise ValueError('Student not found')
        department = Department.objects(abbreviation=department_abbreviation).first()
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
        print(f'Error: The student with this email "{student_email}" is already enrolled in the section "{department_abbreviation} {courseNumber} Section {sectionNumber} ({semester} {sectionYear})".')
    except (db.ValidationError, ValueError) as e:
        print(f'Error adding enrollment: {e}')

def add_student_major():
    try:
        student_email = input("Enter student email: ")
        major_name = input("Enter major name: ")
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

def list_departments():
    departments = Department.objects()
    for department in departments:
        print(department)

def list_courses():
    courses = Course.objects()
    for course in courses:
        print(course)

def list_sections():
    sections = Section.objects()
    for section in sections:
        print(section)

def list_enrollments():
    enrollments = Enrollment.objects()
    for enrollment in enrollments:
        print(enrollment)

def list_students():
    students = Student.objects()
    for student in students:
        print(student)

def list_majors():
    majors = Major.objects()
    for major in majors:
        print(major)

def list_student_majors():
    student_majors = StudentMajor.objects()
    for student_major in student_majors:
        print(student_major)

def list_instructors():
    instructors = Section.objects.distinct('instructor')
    for instructor in sorted(instructors):
        print(instructor)

def delete_department():
    try:
        abbreviation = input("Enter department abbreviation: ")
        department = Department.objects(abbreviation=abbreviation).first()
        if not department:
            raise ValueError('Department not found')
        department.delete()
        print(f'Department deleted: {abbreviation}')
    except ValueError as e:
        print(f'Error deleting department: {e}')

def delete_course():
    try:
        department_abbreviation = input("Enter department abbreviation: ")
        courseNumber = int(input("Enter course number: "))
        department = Department.objects(abbreviation=department_abbreviation).first()
        if not department:
            raise ValueError('Department not found')
        course = Course.objects(department=department, courseNumber=courseNumber).first()
        if not course:
            raise ValueError('Course not found')
        course.delete()
        print(f'Course deleted: {department_abbreviation} {courseNumber}')
    except ValueError as e:
        print(f'Error deleting course: {e}')
#email as ck?
def delete_student():
    try:
        email = input("Enter student email: ")
        student = Student.objects(email=email).first()
        if not student:
            raise ValueError('Student not found')
        student.delete()
        print(f'Student deleted: {email}')
    except ValueError as e:
        print(f'Error deleting student: {e}')

def delete_section():
    try:
        department_abbreviation = input("Enter department abbreviation: ")
        courseNumber = int(input("Enter course number: "))
        sectionNumber = int(input("Enter section number: "))
        semester = input("Enter semester: ")
        sectionYear = int(input("Enter section year: "))
        section = Section.objects(course__department__abbreviation=department_abbreviation, course__courseNumber=courseNumber, sectionNumber=sectionNumber, semester=semester, sectionYear=sectionYear).first()
        if not section:
            raise ValueError('Section not found')
        section.delete()
        print(f'Section deleted: {department_abbreviation} {courseNumber} {sectionNumber} {semester} {sectionYear}')
    except ValueError as e:
        print(f'Error deleting section: {e}')

def delete_major():
    try:
        name = input("Enter major name: ")
        major = Major.objects(name=name)
        if not major:
            raise ValueError('Major not found')
        major.delete()
        print(f'Major deleted:{name}')
    except ValueError as e:
        print(f'Error deleting section: {e}')

def delete_enrollment():
    try:
        student_email = input("Enter student email: ")
        department_abbreviation = input("Enter department abbreviation: ")
        courseNumber = int(input("Enter course number: "))
        sectionNumber = int(input("Enter section number: "))
        semester = input("Enter semester: ")
        sectionYear = int(input("Enter section year: "))
        student = Student.objects(email=student_email).first()
        section = Section.objects(course__department__abbreviation=department_abbreviation, course__courseNumber=courseNumber, sectionNumber=sectionNumber, semester=semester, sectionYear=sectionYear).first()
        if not student or not section:
            raise ValueError('Student or Section not found')
        enrollment = Enrollment.objects(student=student, section=section).first()
        if not enrollment:
            raise ValueError('Enrollment not found')
        enrollment.delete()
        print(f'Enrollment deleted: {student_email} {department_abbreviation} {courseNumber} {sectionNumber} {semester} {sectionYear}')
    except ValueError as e:
        print(f'Error deleting enrollment: {e}')

def delete_student_major():
    try:
        student_email = input("Enter student email: ")
        major_name = input("Enter major name: ")
        student = Student.objects(email=student_email).first()
        major = Major.objects(name=major_name).first()
        if not student or not major:
            raise ValueError('Student or Major not found')
        student_major = StudentMajor.objects(student=student, major=major).first()
        if not student_major:
            raise ValueError('StudentMajor not found')
        student_major.delete()
        print(f'StudentMajor deleted: {student_email} {major_name}')
    except ValueError as e:
        print(f'Error deleting student major: {e}')

def update_department_abbreviation():
    try:
        old_abbreviation = input("Enter current department abbreviation: ")
        new_abbreviation = input("Enter new department abbreviation: ")
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

def update_course_name():
    try:
        department_abbreviation = input("Enter department abbreviation: ")
        courseNumber = int(input("Enter course number: "))
        new_courseName = input("Enter new course name: ")
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

def update_student_name():
    try:
        email = input("Enter student email: ")
        new_lastName = input("Enter new last name: ")
        new_firstName = input("Enter new first name: ")
        student = Student.objects(email=email).first()
        if not student:
            raise ValueError('Student not found')
        student.lastName = new_lastName
        student.firstName = new_firstName
        student.save()
        print(f'Student updated: {student}')
    except (db.ValidationError, ValueError) as e:
        print(f'Error updating student name: {e}')

def main():
    db = Utilities.startup()
    main_action = ''
    while main_action != menu_main.last_action():
        main_action = menu_main.menu_prompt()
        print('next action: ', main_action)
        exec(main_action, globals(), {'db': db})

if __name__ == "__main__":
    main()