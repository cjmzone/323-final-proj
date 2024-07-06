import mongoengine as db
from datetime import datetime
from Student import Student
from Major import Major
"""this is studentmajor"""
class StudentMajor(db.Document):
    student = db.ReferenceField(Student, reverse_delete_rule=db.CASCADE)
    major = db.ReferenceField(Major, reverse_delete_rule=db.CASCADE)
    declarationDate = db.DateTimeField(required=True, default=datetime.now)
    meta = {
        'indexes': [
            {'fields': ('student', 'major'), 'unique': True, 'name': 'student_major_pk'}
        ]
    }

    def __str__(self):
        return f'{self.student} - {self.major}'
