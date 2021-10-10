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
    try:
        page = int(page)
    except ValueError:
        print('Please enter valid type of input(integer)!')
        for book in books:
            if page == book.page:
                books.remove(book)
        addBook()

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
            break


def findByName(name):
    for book in books:
        if name == book.name:
            book.showBookList()
        else:
            print('There is no such a book name in list')
            break


def findByAuthor(author):
    for book in books:
        if author == book.author:
            book.showBookList()
        else:
            print('There is no such an author in list')
            break


def findByID(id):
    for book in books:
        if int(id) == book.id:
            book.showBookList()
        else:
            print('There is no such an ID in list')
            break


def findByPage(pageMin, pageMax):
    pageRange = range(pageMin, pageMax+1)
    for book in books:
        if int(book.page) in pageRange:
            book.showBookList()
        else:
            print('\nThere is no book in this page count range')
            break


def showCommandList():
    print('\nCommand List: \n0-Show Command List \n1-Add a new book \n2-Show book list \n3-Delete a book by ID \n4-Edit a book details by ID \n5-Search a book by book name \n6-Search a book by author \n7-Search a book by ID \n8-Search a book by page range')


print('\nWelcome to "Mini Library" terminal app!?')
print('To see Command List enter "0"')

while True:
    command = input('\nPlease,enter a command: ')

    if command == '1':
        print('\nPlease, enter book details to add a new book:')
        addBook()
    elif command == '2':
        if books:
            for book in books:
                book.showBookList()
        else:
            print('Sorry, but there is no book in the list now')

    elif command == '3':
        if books:
            id = input('\nEnter the book ID to delete the book: ')
            removeBook(id)
        else:
            print('Sorry, but there is no book in the list now')
    elif command == '4':
        if books:
            id = input('\nEnter a book ID to edit: ')
            editBook(id)
        else:
            print('Sorry, but there is no book in the list now')
    elif command == '5':
        if books:
            name = input('\nEnter a book name to search: ')
            findByName(name)
        else:
            print('Sorry, but there is no book in the list now')
    elif command == '6':
        if books:
            author = input('\nEnter an author to search: ')
            findByAuthor(author)
        else:
            print('Sorry, but there is no book in the list now')
    elif command == '7':
        if books:
            id = input('\nEnter a book ID to search: ')
            findByID(id)
        else:
            print('Sorry, but there is no book in the list now')
    elif command == '8':
        if books:
            pageMin = int(input('\nEnter minimum page quantity to search: '))
            pageMax = int(input('Enter maximum page quantity to search: '))
            findByPage(pageMin, pageMax)
        else:
            print('Sorry, but there is no book in the list now')
    elif command == '0':
        showCommandList()
    else:
        print('\nPlease, enter right command! (For commands, check Command List) \nTo see Command List enter "0" ')
