names = []
surnames = []
ageLst = []
emails = []
userList = [names, surnames, ageLst, emails]

while True:

    ask = input('For adding new user enter "1" or To see user list enter "2": ')

    if ask == '1':
        name = input('Enter user name: ')
        names.append(name)
        surname = input('Enter user surname: ')
        surnames.append(surname)
        age = input('Enter age: ')
        ageLst.append(age)
        email = input('Enter email: ')
        emails.append(email)

    elif ask == '2':
        for x in userList:
            if x:
                print(x)
            else:
                print('There is no user now')
                break
