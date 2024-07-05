import mongoengine as db
from .department import Department

class Course(db.Document):
    department = db.ReferenceField(Department, reverse_delete_rule=db.CASCADE)
    courseNumber = db.IntField(required=True, min_value=100, max_value=699)
    courseName = db.StringField(required=True, max_length=100)
    units = db.IntField(required=True, min_value=1, max_value=5)
    meta = {
        'indexes': [
            {'fields': ['department', 'courseNumber'], 'unique': True},
            {'fields': ['department', 'courseName'], 'unique': True}
        ]
    }

    def __str__(self):
        return f'{self.department.abbreviation} {self.courseNumber}: {self.courseName}'
