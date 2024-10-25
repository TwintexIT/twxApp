import sqlite3
import pyodbc

groceries = [
	"Ivo",
	"Pedro",
	"Mico",
]

groceries = sorted(groceries)

connection = pyodbc.connect(driver='{SQL Server}',
                               server='SRVMOD\TWINTEX2008R2',
                               database='Tutor_TWX_testes',
                               uid='sa',pwd='TWXsql#05')
cursor = connection.cursor()

'''cursor.execute("create table teste (id INTEGER PRIMARY KEY identity(1,1), nome TEXT)")'''

for i in range(len(groceries)):
	cursor.execute("insert into teste (nome) values (?)",[groceries[i]])
	print("added ", groceries[i])

connection.commit()
connection.close()