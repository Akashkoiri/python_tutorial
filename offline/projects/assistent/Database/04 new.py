import mysql.connector as sql

mydb = sql.connect(
    host='127.0.0.1',
    user='root',
    password='akash182639',
    database='test'
)

cursor = mydb.cursor()

# cursor.execute("describe students1")
# cursor.execute("insert into students1(id,name,age) values(4,'kabir',40)")
cursor.execute("select * from students1")

for i in cursor:
    print(i)

# mydb.commit()