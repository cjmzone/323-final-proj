import mongoengine as db
from Department import Department
"""this is major"""
class Major(db.Document):
    department = db.ReferenceField(Department, reverse_delete_rule=db.CASCADE)
    name = db.StringField(required=True, max_length=100)
    meta = {
        'indexes': [
            {'fields': ['name'], 'unique': True, 'name': 'major_pk'}
        ]
    }

    def __str__(self):
        return f'{self.department.name}: {self.name}'