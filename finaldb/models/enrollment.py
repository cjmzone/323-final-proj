import mongoengine as db
from .student import Student
from .section import Section

class Enrollment(db.Document):
    student = db.ReferenceField(Student, reverse_delete_rule=db.CASCADE)
    section = db.ReferenceField(Section, reverse_delete_rule=db.CASCADE)
    category = db.StringField(required=True, choices=['PassFail', 'LetterGrade'])
    meta = {
        'indexes': [
            {'fields': ['student', 'section'], 'unique': True},
            {'fields': ['student', 'section', 'category'], 'unique': True}
        ]
    }

    def __str__(self):
        return f'{self.student} enrolled in {self.section}'
