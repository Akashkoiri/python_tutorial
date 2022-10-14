import mysql.connector as sql

mydb = sql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'akash182639',
    database = 'test'
)

cursor = mydb.cursor()

## if data is 1:
# data = (1,'akash',20)
# cursor.execute("insert into students(id,name,age) values(%s,%s,%s)",data)

## if data is more than 1:
data = [(1,'akash',20),
        (2,'bikash',30),
        (3,'sagar',10),
        (4,'sujal',40)]

cursor.executemany("insert into students(id,name,age) values(%s,%s,%s)",data)

# deleting a record
# cursor.execute("delete from students where id < 5 and id > 1")

# this command is mendetory for applying the changes
mydb.commit()
