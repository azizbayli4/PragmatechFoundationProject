users = []


def createUser():
    _ad = input('Ad: ')
    _soyad = input('Soyad: ')
    _yas = input('Yas: ')
    _email = input('Email: ')

    user = {
        'ad': _ad,
        'soyad': _soyad,
        'yas': _yas,
        'email': _email
    }

    users.append(user)


while True:
    emr = input('Tamam mi davam mi (T/D): ')

    if emr == 'T':
        print(users)
        break
    else:
        createUser()
