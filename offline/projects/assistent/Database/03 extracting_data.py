import mysql.connector as sql

mydb = sql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'akash182639',
    database = 'phonebook'
)
cursor = mydb.cursor()


# getting data from db
# cursor.execute('select id from students1')

# using where clause
# cursor.execute('select * from students1 WHERE age >= 15 and age <= 25 ')

# using wildcard charector(to find some substring)
cursor.execute("select * from phonebook")


# saving all data into a list
all_data = cursor.fetchall()

# saving only first feild(row)
# first_data = cursor.fetchone()


for i in all_data:
    print(i)