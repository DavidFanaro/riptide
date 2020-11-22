from app import db
from uuid import uuid4

class User(db.Model):
    id = db.Column(db.Text(), primary_key=True)
    username = db.Column(db.Text(), unique=True, nullable=False)
    email = db.Column(db.Text(), unique=True, nullable=False)
    firstname = db.Column(db.Text(), unique=True, nullable=False)
    lastname = db.Column(db.Text(), unique=True, nullable=False)
    password = db.Column(db.Text(), unique=True, nullable=False)

    def __init__ (self, username, email, firstname, lastname, password):
        self.id = uuid4().hex
        self.username = username
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password

        