from  flask_sqlalchemy import SQLAlchemy
from app import app, db

db = SQLAlchemy(app)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    education = db.Column(db.String(255))
    occupation = db.Columm(db.String(255))
    experience = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    num_children = db.Column(db.Integer)