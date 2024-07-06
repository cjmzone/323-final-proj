import mongoengine as db
from Course import Course
"""this is section :^)"""
class Section(db.Document):
    course = db.ReferenceField(Course, reverse_delete_rule=db.CASCADE)
    sectionNumber = db.IntField(required=True)
    semester = db.StringField(required=True, choices=['Fall', 'Spring', 'Summer I', 'Summer II', 'Summer III', 'Winter'])
    sectionYear = db.IntField(required=True)
    building = db.StringField(required=True, choices=['ANAC', 'CDC', 'DC', 'ECS', 'EN2', 'EN3', 'EN4', 'EN5', 'ET', 'HSCI', 'NUR', 'VEC'])
    room = db.IntField(required=True, min_value=1, max_value=999)
    schedule = db.StringField(required=True, choices=['MW', 'TuTh', 'MWF', 'F', 'S'])
    startTime = db.DateTimeField(required=True)
    instructor = db.StringField(max_length=100)
    meta = {
        'indexes': [
            {'fields': ['course', 'sectionNumber', 'semester', 'sectionYear'], 'unique': True, 'name': 'section_pk'},
            {'fields': ['semester', 'sectionYear', 'building', 'room', 'startTime'], 'unique': True, 'name': 'section_uk_01'},
            {'fields': ['semester', 'sectionYear', 'instructor', 'startTime'], 'unique': True, 'name': 'section_uk_02'}
        ]
    }
    def __str__(self):
        return f'{self.course} Section {self.sectionNumber} ({self.semester} {self.sectionYear})'
