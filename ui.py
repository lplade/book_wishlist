# from book import Book


def display_menu_get_choice():

    """Display choices for user, return users' selection"""

    print('''
        1. Show unread books (wishlist)
        2. Show books that have been read
        3. Mark a book as read
        4. Add book to wishlist
        5. Delete book from list
        6. Edit book title & author
        7. Rate book
        8. Search for a book
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice


def show_list(books):
    """ Format and display a list of book objects"""

    if len(books) == 0:
        print('* No books *')
        return

    for book in books:
        print(book)

    print('* {} book(s) *'.format(len(books)))


def ask_for_book_id():
    """ Ask user for book id, validate to ensure it is a positive integer """

    while True:
        try:
            book_id = int(input('Enter book id: '))
            if book_id >= 0:
                return book_id
            else:
                print('Please enter a positive number')
        except ValueError:
            print('Please enter an integer number')


def confirm_new_book():
    command = input('Book already in read list! \"Y\" to continue: ')
    command.upper()
    if command == 'Y' or command == 'YES':
        return True
    else:
        return False


def ask_for_date_read():
    # TODO implement this
    pass


def get_new_book_information():
    """Get new title for book"""
    title = input('Enter new title: ')
    author = input('Enter new author: ')
    return title, author


def get_book_rating():
    """Get rating for book"""
    low, high = 0, 5
    while True:
        try:
            rating = int(input('How would you rate this book? (0-5) '))
            if low <= rating <= high:
                return rating
            else:
                print('Value out of range.')
        except ValueError:
            print('Must enter a valid number.')


def get_book_info():
    """ Get title and author of new book from user """
    title = input('Enter title: ')
    author = input('Enter author: ')
    return title, author


def message(msg):
    """Display a message to the user"""
    print(msg)
