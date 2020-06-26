from venv import db

class Result(db.Document):
    iid=db.StringField(max_length=50)
    res=db.StringField(max_length=50)

class Size(db.Document):
    iid = db.StringField(max_length=50)
    size = db.StringField(max_length=50)

