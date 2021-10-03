from flask import Flask

SQLALCHEMY_DATABASE_URI = 'mssql://GraceVM/SQLAlchemyDB?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
SQLALCHEMY_TRACK_MODIFICATIONS = False