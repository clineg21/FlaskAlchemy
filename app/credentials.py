from flask import Flask
# import pydoc

# SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://GraceVM/SQLAlchemyDB?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Romans8.23@localhost/SQLAlchemyDB'
SQLALCHEMY_TRACK_MODIFICATIONS = False