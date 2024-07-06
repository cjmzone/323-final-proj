from models.department import Department
from models.course import Course
from models.student import Student
from models.section import Section
from models.enrollment import Enrollment
from models.student_major import StudentMajor
from models.major import Major

def delete_department(abbreviation):
    try:
        department = Department.objects(abbreviation=abbreviation).first()
        if not department:
            raise ValueError('Department not found')
        department.delete()
        print(f'Department deleted: {abbreviation}')
    except ValueError as e:
        print(f'Error deleting department: {e}')

def delete_course(department_abbreviation, courseNumber):
    try:
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

def delete_student(email):
    try:
        student = Student.objects(email=email).first()
        if not student:
            raise ValueError('Student not found')
        student.delete()
        print(f'Student deleted: {email}')
    except ValueError as e:
        print(f'Error deleting student: {e}')

def delete_section(course_abbreviation, courseNumber, sectionNumber, semester, sectionYear):
    try:
        section = Section.objects(course__department__abbreviation=course_abbreviation, course__courseNumber=courseNumber, sectionNumber=sectionNumber, semester=semester, sectionYear=sectionYear).first()
        if not section:
            raise ValueError('Section not found')
        section.delete()
        print(f'Section deleted: {course_abbreviation} {courseNumber} {sectionNumber} {semester} {sectionYear}')
    except ValueError as e:
        print(f'Error deleting section: {e}')

def delete_enrollment(student_email, course_abbreviation, courseNumber, sectionNumber, semester, sectionYear):
    try:
        student = Student.objects(email=student_email).first()
        section = Section.objects(course__department__abbreviation=course_abbreviation, course__courseNumber=courseNumber, sectionNumber=sectionNumber, semester=semester, sectionYear=sectionYear).first()
        if not student or not section:
            raise ValueError('Student or Section not found')
        enrollment = Enrollment.objects(student=student, section=section).first()
        if not enrollment:
            raise ValueError('Enrollment not found')
        enrollment.delete()
        print(f'Enrollment deleted: {student_email} {course_abbreviation} {courseNumber} {sectionNumber} {semester} {sectionYear}')
    except ValueError as e:
        print(f'Error deleting enrollment: {e}')

def delete_student_major(student_email, major_name):
    try:
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
