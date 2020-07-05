from .db import db


class Entree(db.Document):
    name = db.StringField(required=True, unique=True)
    wines = db.ListField(db.StringField(), required=False)
    allergens = db.ListField(db.StringField(), required=False)
