import mongoengine as db
"""this is the department """
class Department(db.Document):
    name = db.StringField(required=True, max_length=80)
    abbreviation = db.StringField(required=True, max_length=6)
    chairName = db.StringField(required=True, max_length=80)
    building = db.StringField(required=True, choices=['ANAC', 'CDC', 'DC', 'ECS', 'EN2', 'EN3', 'EN4', 'EN5', 'ET', 'HSCI', 'NUR', 'VEC'])
    office = db.StringField(required=True)
    description = db.StringField(max_length=80)
    meta = {
        'indexes': [
            {'fields': ['name'], 'unique': True, 'name': 'department_pk'},
            {'fields': ['abbreviation'], 'unique': True, 'name': 'department_uk_01'},
            {'fields': ['chairName'], 'unique': True, 'name': 'department_uk_02'},
            {'fields': ['building', 'office'], 'unique': True, 'name': 'department_uk_03'}
        ]
    }

    def __str__(self):
        return f'Department:{self.name} ({self.abbreviation}) Chairman:{self.chairName} Building: {self.building} {self.office}'
