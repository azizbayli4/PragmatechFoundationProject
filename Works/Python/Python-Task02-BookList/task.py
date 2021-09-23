books = []


class Book:
    def __init__(self, _id, _name, _author, _page):
        self.id = _id
        self.name = _name
        self.author = _author
        self.page = _page

    def adToList(self):
        books.append(self)

    def showBookList(self):
        print(
            f'ID: {self.id}, Book name: {self.name}, Author: {self.author}, Page count: {self.page} ')


id = 0


def addBook():
    global id
    id = id + 1
    name = input('Name: ')
    author = input('Author: ')
    page = input('Page: ')

    book = Book(id, name, author, page)
    book.adToList()


def removeBook(id):
    for book in books:
        if int(id) == book.id:
            books.remove(book)
            break


def editBook(id):
    for book in books:
        if int(id) == book.id:
            book.id = input('Enter new ID: ')
            book.name = input('Enter new name: ')
            book.author = input('Enter new author: ')
            book.page = input('Enter new page: ')


def findByName(name):
    for book in books:
        if name == book.name:
            book.showBookList()
            break


def findByID(id):
    for book in books:
        if int(id) == book.id:
            book.showBookList()
            break


while True:
    command = input('Enter Command: ')

    if command == '1':
        addBook()
    elif command == '2':
        for book in books:
            book.showBookList()
    elif command == '3':
        id = input('Enter book ID which will delete: ')
        removeBook(id)
    elif command == '4':
        id = input('Enter book ID to edit: ')
        editBook(id)
    elif command == '5':
        name = input('Enter book name to search: ')
        findByName(name)
    elif command == '6':
        id = input('Enter book ID to search: ')
        findByID(id)
