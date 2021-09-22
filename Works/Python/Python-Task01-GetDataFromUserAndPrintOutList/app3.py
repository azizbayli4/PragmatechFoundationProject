
userList = []

while True:

    ask = input('For adding new user enter "1" or To see user list enter "2": ')

    if ask == '1':
        name = input('Enter user name: ')
        surname = input('Enter user surname: ')
        age = input('Enter age: ')
        email = input('Enter email: ')
        userList.extend(['Name: ' + name, 'Surname: ' +
                        surname, 'Age: ' + age, 'Email: ' + email])

    elif ask == '2':
        if userList:
            print(userList)
            break
        else:
            print('There is no user now')
