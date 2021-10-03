from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import insert, select, update
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql://GraceVM/SQLAlchemyDB?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)

metadata = MetaData()
metadata.reflect(engine, only=['account', 'account_history'])
Base = automap_base(metadata=metadata)

connection = engine.connect()
Base.prepare(engine, reflect=True)

account_table = Table('account', metadata, autoload=True)
account_history_table = Table('account_history', metadata, autoload=True)


@app.route('/')
@app.route('/home')
def hello():
    account_query = select([account_table])
    account_result = connection.execute(account_query)
    account_json = jsonify({'accountResult': [dict(row) for row in account_result]})
    return account_json

