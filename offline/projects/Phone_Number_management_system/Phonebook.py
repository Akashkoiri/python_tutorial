.phonebook = {}

def register():
    name = input('Enter name: ')
    number = int(input('Enter number: '))
    phonebook[name] = number
    print('\n')

exit = False

while not exit:
    ans = int(input('1. Search\n2. Add\n3. show all\n4. Exit\nEnter your choice: '))

    if ans==1:
        ser_name = input('Enter name: ')
        if ser_name in phonebook:
            print(f'Number: {phonebook[ser_name]}\n')
    elif ans==2:
        register()
    elif ans==3:
        print('\nName\tNumber')
        for name in phonebook:
            print(name,'\t',phonebook[name])
        print('\n')
    elif ans==4:
        exit = True
    else:
        print('\nWrong choice...\nTry again.')

