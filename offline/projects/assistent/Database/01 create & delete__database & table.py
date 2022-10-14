import mysql.connector as sql

mydb = sql.connect(
    host='127.0.0.1',
    user='root',                
    password='akash182639',
    database = 'test'
)
# print(mydb.connection_id)
cursor = mydb.cursor()
# print(type(cursor))
cursor.execute('show databases')
# cursor.execute('create database test')
# cursor.execute('drop database test')
# cursor.execute('create table students(name varchar(255),age int(10))')
# cursor.execute('show tables')
# cursor.execute('describe students')
# cursor.execute('drop table students')


for i in cursor:
    print(i)


# print("DONE")