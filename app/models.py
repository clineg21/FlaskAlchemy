from sqlalchemy import ForeignKey
from datetime import datetime
from app import db, engine
from sqlalchemy.orm import sessionmaker

class Accounts(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    account_number = db.Column(db.Integer, unique=True, nullable=False)
    ssn = db.Column(db.String(30), unique=True, nullable=False)
    account_history = db.relationship("Account_History", backref=db.backref('account_history'))

    def __repr__(self):
        return f"Accounts('{self.first_name}', '{self.last_name}', '{self.account_number}', '{self.ssn}')"

class Account_History(db.Model):
    __tablename__ = 'account_history'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, ForeignKey('accounts.id'))
    date_changed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"Account_History('{self.account_id}', '{self.date_changed}')"

db.create_all()

Session = sessionmaker(bind = engine)
session = Session()
