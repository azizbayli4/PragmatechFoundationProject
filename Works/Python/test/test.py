users = []


class User:
    def __init__(self, _ad, _soyad, _yas, _email):
        self.ad = _ad
        self.soyad = _soyad
        self.yas = _yas
        self.email = _email

    def addToList(self):
        users.append(self)

    def showUser(self):
        print(f'{self.ad},{self.soyad},{self.yas},{self.email} ')


def createUser():
    ad = input('Ad: ')
    soyad = input('Soyad: ')
    yas = input('Yas: ')
    email = input('Email: ')

    user = User(ad, soyad, yas, email)
    user.addToList()


while True:
    emr = input('Tamam mi davam mi (T/D): ')

    if emr == 'T':
        for user in users:
            user.showUser()
        break
    elif emr == 'D':
        createUser()
    else:
        print('Duzgun komanda daxil edin')
