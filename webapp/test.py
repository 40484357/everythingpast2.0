import sqlalchemy as sql

engine = sql.create_engine('mssql+pyodbc://WINDOWS-PC/test?Trusted_Connection=yes&')