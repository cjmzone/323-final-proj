import mongoengine as db
from Student import Student
from Section import Section
"""this is enrollment"""
class Enrollment(db.Document):
    student = db.ReferenceField(Student, reverse_delete_rule=db.CASCADE)
    section = db.ReferenceField(Section, reverse_delete_rule=db.CASCADE)
    category = db.StringField(required=True, choices=['PassFail', 'LetterGrade'])
    minSatisfactory = db.StringField(choices=['A','B','C'])
    meta = {
        'indexes': [
            {'fields': ['student', 'section'], 'unique': True, 'name': 'enrollment_pk'}
        ]
    }

    def __str__(self):
        return f'{self.student} enrolled in {self.section}'
