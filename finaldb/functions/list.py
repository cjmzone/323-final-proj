from models.department import Department
from models.course import Course
from models.section import Section
from models.enrollment import Enrollment
from models.student import Student
from models.major import Major

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

def list_instructors():
    instructors = Section.objects.distinct('instructor')
    for instructor in sorted(instructors):
        print(instructor)
