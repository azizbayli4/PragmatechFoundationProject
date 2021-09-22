names = []
surnames = []
ageLst = []
emails = []

while True:

    ask = input('For adding new user enter "1" or To see user list enter "2": ')
    # ask2 = input('To see user list enter "2": ')

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
        for x in names:
            print('Name: ' + x)
        for y in surnames:
            print('Surname: ' + y)
        for z in ageLst:
            print('Age: ' + z)
        for j in emails:
            print('Email: ' + j)
