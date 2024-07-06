import mongoengine as db
from datetime import datetime
from .student import Student
from .major import Major
"""this is studentmajor"""
class StudentMajor(db.Document):
    student = db.ReferenceField(Student, reverse_delete_rule=db.CASCADE)
    major = db.ReferenceField(Major, reverse_delete_rule=db.CASCADE)
    declarationDate = db.DateTimeField(required=True, default=datetime.now)
    meta = {
        'indexes': [
            {'fields': ('student', 'major'), 'unique': True}
        ]
    }

    def __str__(self):
        return f'{self.student} - {self.major}'
