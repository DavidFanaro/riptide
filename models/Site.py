from app import db
from uuid import uuid4

class Site(db.Model):
    id = db.Column(db.Text(), primary_key=True)
    user_id = db.Column(db.Text(), db.ForeignKey('user.id'))
    siteName = db.Column(db.Text(), unique=True, nullable=False)
    siteUrl = db.Column(db.Text(), unique=True, nullable=False)
    sitePassword = db.Column(db.Text(), unique=True, nullable=False)
    siteImage = db.Column(db.Integer(), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, user_id:str, siteName, siteUrl, sitePassword, siteImage:int):
        self.id = uuid4().hex
        self.user_id = user_id
        self.siteName = siteName
        self.siteUrl = siteUrl
        self.sitePassword = sitePassword
        self.siteImage = siteImage