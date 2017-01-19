from book import Book


def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show unread books (wishlist)
        2. Show books that have been read
        3. Mark a book as read
        4. Add book to wishlist
        5. Remove book from wishlist
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice


def show_list(books):
    """
    Format and display a list of book objects
    :type books: list of Book
    :return:
    """

    if len(books) == 0:
        print('* No books *')
        return

    for book in books:
        print(book)

    print('* {} book(s) *'.format(len(books)))


def ask_for_book_id():
    """
    Ask user for book id, validate to ensure it is a positive integer
    :rtype: int
    """

    while True:
        try:
            book_id = int(input('Enter book id:'))
            if book_id >= 0:
                return book_id
            else:
                print('Please enter a positive number ')
        except ValueError:
            print('Please enter an integer number')


def get_new_book_info():

    ''' Get title and author of new book from user '''

    title = input('Enter title: ')
    author = input('Enter author: ')
    return Book(title, author)


def message(msg):
    '''Display a message to the user'''
    print(msg)
