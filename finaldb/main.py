import mongoengine as me
from datetime import datetime
from functions.add import add_department, add_course, add_major, add_student, add_section, add_enrollment, add_student_major
from functions.list import list_departments, list_courses, list_sections, list_enrollments, list_students, list_majors, list_instructors
from functions.delete import delete_department, delete_course, delete_student, delete_section, delete_enrollment, delete_student_major
from functions.update import update_department_abbreviation, update_course_name, update_student_name
# Establish connection to MongoDB

me.connect(db='school', host='mongodb+srv://cjmzone:wireWar21$@cecs323.dp4wxsa.mongodb.net/?retryWrites=true&w=majority&appName=cecs323')

def add_menu():
    while True:
        print("\nAdd Options:")
        print("1. Add Department")
        print("2. Add Course")
        print("3. Add Major")
        print("4. Add Student")
        print("5. Add Section")
        print("6. Add Enrollment")
        print("7. Add Student Major")
        print("8. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter department name: ")
            abbreviation = input("Enter department abbreviation: ")
            chairName = input("Enter chair name: ")
            building = input("Enter building: ")
            office = input("Enter office: ")
            description = input("Enter description: ")
            add_department(name, abbreviation, chairName, building, office, description)
       
        elif choice == '2':
            department_abbreviation = input("Enter department abbreviation: ")
            courseNumber = int(input("Enter course number: "))
            courseName = input("Enter course name: ")
            units = int(input("Enter units: "))
            add_course(department_abbreviation, courseNumber, courseName, units)
        
        elif choice == '3':
            name = input("Enter major name: ")
            add_major(name)
        
        elif choice == '4':
            lastName = input("Enter last name: ")
            firstName = input("Enter first name: ")
            email = input("Enter email: ")
            add_student(lastName, firstName, email)
       
        elif choice == '5':
            course_abbreviation = input("Enter course abbreviation: ")
            courseNumber = int(input("Enter course number: "))
            sectionNumber = int(input("Enter section number: "))
            semester = input("Enter semester: ")
            sectionYear = int(input("Enter section year: "))
            building = input("Enter building: ")
            room = int(input("Enter room: "))
            schedule = input("Enter schedule: ")
            startTime = datetime.strptime(input("Enter start time (HH:MM): "), '%H:%M')
            instructor = input("Enter instructor: ")
            add_section(course_abbreviation, courseNumber, sectionNumber, semester, sectionYear, building, room, schedule, startTime, instructor)
        
        elif choice == '6':
            student_email = input("Enter student email: ")
            course_abbreviation = input("Enter course abbreviation: ")
            courseNumber = int(input("Enter course number: "))
            sectionNumber = int(input("Enter section number: "))
            semester = input("Enter semester: ")
            sectionYear = int(input("Enter section year: "))
            category = input("Enter category (PassFail/LetterGrade): ")
            add_enrollment(student_email, course_abbreviation, courseNumber, sectionNumber, semester, sectionYear, category)
       
        elif choice == '7':
            student_email = input("Enter student email: ")
            major_name = input("Enter major name: ")
            add_student_major(student_email, major_name)
        
        elif choice == '8':
            break
        else:
            print("Invalid choice, please try again.")

def list_menu():
    while True:
        print("\nList Options:")
        print("1. List Department")
        print("2. List Courses")
        print("3. List Sections")
        print("4. List Enrollments")
        print("5. List Students")
        print("6. List Majors")
        print("7. List Instructors")
        print("8. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            list_departments()
        elif choice == '2':
            list_courses()
        elif choice == '3':
            list_sections()
        elif choice == '4':
            list_enrollments()
        elif choice == '5':
            list_students()
        elif choice == '6':
            list_majors()
        elif choice == '7':
            list_instructors()
        elif choice == '8':
            break
        else:
            print("Invalid choice, please try again.")

def delete_menu():
    while True:
        print("\nDelete Options:")
        print("1. Delete Department")
        print("2. Delete Course")
        print("3. Delete Student")
        print("4. Delete Section")
        print("5. Delete Enrollment")
        print("6. Delete Student Major")
        print("7. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            abbreviation = input("Enter department abbreviation: ")
            delete_department(abbreviation)
        
        elif choice == '2':
            department_abbreviation = input("Enter department abbreviation: ")
            courseNumber = int(input("Enter course number: "))
            delete_course(department_abbreviation, courseNumber)
        
        elif choice == '3':
            email = input("Enter student email: ")
            delete_student(email)
     
        elif choice == '4':
            course_abbreviation = input("Enter course abbreviation: ")
            courseNumber = int(input("Enter course number: "))
            sectionNumber = int(input("Enter section number: "))
            semester = input("Enter semester: ")
            sectionYear = int(input("Enter section year: "))
            delete_section(course_abbreviation, courseNumber, sectionNumber, semester, sectionYear)
        
        elif choice == '5':
            student_email = input("Enter student email: ")
            course_abbreviation = input("Enter course abbreviation: ")
            courseNumber = int(input("Enter course number: "))
            sectionNumber = int(input("Enter section number: "))
            semester = input("Enter semester: ")
            sectionYear = int(input("Enter section year: "))
            delete_enrollment(student_email, course_abbreviation, courseNumber, sectionNumber, semester, sectionYear)
      
        elif choice == '6':
            student_email = input("Enter student email: ")
            major_name = input("Enter major name: ")
            delete_student_major(student_email, major_name)
        
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")
            
def update_menu():
    while True:
        print("\nUpdate Options:")
        print("1. Change Department Abbreviation")
        print("2. Change Course Name")
        print("3. Change Student Name")
        print("4. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            old_abbreviation = input("Enter current department abbreviation: ")
            new_abbreviation = input("Enter new department abbreviation: ")
            update_department_abbreviation(old_abbreviation, new_abbreviation)
        elif choice == '2':
            department_abbreviation = input("Enter department abbreviation: ")
            courseNumber = int(input("Enter course number: "))
            new_courseName = input("Enter new course name: ")
            update_course_name(department_abbreviation, courseNumber, new_courseName)
        elif choice == '3':
            email = input("Enter student email: ")
            new_lastName = input("Enter new last name: ")
            new_firstName = input("Enter new first name: ")
            update_student_name(email, new_lastName, new_firstName)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def main():
    while True:
        print("\nMain Menu:")
        print("1. Add")
        print("2. List")
        print("3. Delete")
        print("4. Update")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_menu()
        elif choice == '2':
            list_menu()
        elif choice == '3':
            delete_menu()
        elif choice == '4':
            update_menu()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()