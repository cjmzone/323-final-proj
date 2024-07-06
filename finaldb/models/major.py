import mongoengine as db
"""this is major"""
class Major(db.Document):
    name = db.StringField(required=True, unique=True, max_length=100)

    def __str__(self):
        return self.name
