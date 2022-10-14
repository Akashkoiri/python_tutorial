import mysql.connector as sql

mydb = sql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'akash182639',
    database = 'phonebook' 
)
cursor = mydb.cursor()

exit = False

def search():
    cursor.execute('select * from phonebook')
    return cursor.fetchall()

def register():
    name = input('Enter name(Max: 12 words): ').lower()
    number = int(input('Enter number: '))
    
    data = (name,number)
    cursor.execute("insert into phonebook(name,number) values(%s,%s)",data)


while not exit:
    ans = int(input('1. Search\n2. Add\n3. show all\n4. Delet\n5. Exit\nEnter your choice: '))

    if ans==1:
        ser_name = input('Enter name: ').lower()
        all_data = search()

        for i in all_data:
            if i[0] == ser_name:
                print(f'\nNumber: {i[1]}\n')
            else:
                print("\nCan't find that name...\n")
                
    elif ans==2:
        register()
        mydb.commit()

    elif ans==3:
        print('\nName\t          Number')
        print('----------------------------')
        
        phonebook = list(search())

        for name in phonebook:
            print(name[0],'  \t|',name[1])

        print('\n')

    elif ans==4:
        pass

    elif ans==5:
        exit = True

    else:
        print('\nWrong choice\nTry again...\n')

