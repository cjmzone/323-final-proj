from Menu import Menu
from Option import Option

"""
This little file just has the menus declared.  Each variable (e.g. menu_main) has 
its own set of options and actions.  Although, you'll see that the "action" could
be something other than an operation to perform.

Doing the menu declarations here seemed like a cleaner way to define them.  When
this is imported in main.py, these assignment statements are executed and the 
variables are constructed.  To be honest, I'm not sure whether these are global
variables or not in Python.
"""

# The main options for operating on Departments and Courses.
menu_main = Menu('main', 'Please select one of the following options:', [
    Option("Add", "add(db)"),
    Option("List", "list_objects(db)"),
    Option("Delete", "delete(db)"),
    Option("Update", "update(db)"),
    #    Option("Boilerplate Data", "boilerplate(db)"),
    Option("Exit this application", "pass")
])

add_menu = Menu('add', 'Please indicate what you want to add:', [
    Option("Department", "add_department()"),
    Option("Course", "add_course()"),
    Option("Section", "add_section()"),
    Option("Major", "add_major()"),
    Option("Student", "add_student()"),
    Option("Student to Major", "add_student_major()"),
    Option("Enrollment", "add_enrollment()"),
    Option("Exit", "pass")
])

delete_menu = Menu('delete', 'Please indicate what you want to delete from:', [
    Option("Department", "delete_department()"),
    Option("Course", "delete_course()"),
    Option("Section", "delete_section()"),
    Option("Major", "delete_major()"),
    Option("Student", "delete_student()"),
    Option("Student to Major", "delete_student_major()"),
    Option("Enrollment", "delete_enrollment()"),
    Option("Exit", "pass")
])

list_menu = Menu('list', 'Please indicate what you want to list:', [
    Option("Department", "list_departments()"),
    Option("Course", "list_courses()"),
    Option("Sections", "list_sections()"),
    Option("Major", "list_majors()"),
    Option("Student", "list_students()"),
    Option("Student to Major", "list_student_majors()"),
    Option("Enrollment", "list_enrollments()"),
    Option("Instructor", "list_instructors()"),
    Option("Exit", "pass")
])

update_menu = Menu('update', 'Please indicate what you want to update:', [
    Option("Department Abbreviation", "update_department_abbreviation()"),
    Option("Course Name", "update_course_name()"),
    Option("Student Name", "update_student_name()"),
    Option("Exit", "pass")
])