import mongoengine as db

class Student(db.Document):
    lastName = db.StringField(required=True, max_length=80)
    firstName = db.StringField(required=True, max_length=80)
    email = db.EmailField(required=True, unique=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
