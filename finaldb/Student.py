import mongoengine as db
"""this is student"""
class Student(db.Document):
    lastName = db.StringField(required=True, max_length=80)
    firstName = db.StringField(required=True, max_length=80)
    email = db.EmailField(required=True, unique=True)
    meta = {
        'indexes': [
            {'fields': ['lastName', 'firstName'], 'unique': True, 'name': 'student_pk'},
            {'fields': ['email'], 'unique': True, 'name': 'student_uk_01'}
        ]
    }
    def __str__(self):
        return f'{self.firstName} {self.lastName}'
