import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Gcameae032$'
)

cursorobject = database.cursor()

cursorobject.execute('CREATE DATABASE mydatabase')

print('all done')