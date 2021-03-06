import os
import file_io

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

book_list = []
counter = 0


def setup():
    """ Read book info from file, if file exists. """

    global counter, book_list

    book_list.extend(file_io.read_file(BOOKS_FILE_NAME))
    counter = file_io.read_file_int(COUNTER_FILE_NAME, book_list)


def shutdown():
    """
    Save all data to a file -
    one for books, one for the current counter value, for persistent storage
    """
    output_data = make_output_data()
    # Create data directory
    file_io.check_dir(DATA_DIR)
    # write to book, counter files
    file_io.write_file(BOOKS_FILE_NAME, output_data)
    file_io.write_file(COUNTER_FILE_NAME, str(counter))


def get_books(**kwargs):
    ''' Return books from data store. With no arguments, returns everything. '''

    global book_list
    if len(kwargs) == 0:
        return book_list
    if 'read' in kwargs:
        read_books = [book for book in book_list if book.read == kwargs['read']]
        return read_books


def check_book(book_title, book_author):
    read_list = get_books(read=True)

    for book in read_list:
        if book.title == book_title \
                or book.author == book_author:
            return True

    return False


def add_book(book):
    ''' Add to db, set id value, return Book'''

    global book_list

    book.book_id = generate_id()
    book_list.append(book)


def find_book(book_title, book_author):
    global book_list

    book = [
        book for book in book_list
        if book.title == book_title or book.author == book_author
        ]

    return book


def generate_id():
    global counter
    counter += 1
    return counter


def delete_book(book_id):
    """
    Delete book with given book_id. Return True if found, False otherwise.
    :type book_id: int
    :rtype: bool
    """
    global book_list

    for book in book_list:
        if book.book_id == book_id:
            book_list.remove(book)  # remove matching book from list
            return True

    return False  # return False if book id is not found


def set_book_information(book_id, new_title, new_author):
    '''Set book object title to new_title parameter'''
    global book_list

    for book in book_list:
        if book.book_id == book_id:
            book.title, book.author = new_title, new_author


def set_book_rating(book_id, rating):
    global book_list

    for book in book_list:
        if book.id == book_id:
            book.rating = rating


def set_read(book_id, date_read, read):
    """
    Update book with given book_id to read. Return True if book is found
    in DB and update is made, False otherwise.
    :type book_id: int
    :type date_read: datetime.date
    :type read: bool
    """

    global book_list

    for book in book_list:

        if book.book_id == book_id:
            book.read = True
            book.set_date_read(date_read)
            return True

    return False  # return False if book id is not found


def make_output_data():
    """
    create a string containing all data on books, for writing to output file
    """

    global book_list

    output_data = []

    for book in book_list:
        output_line = book.to_json()
        output_data.append(output_line)

    all_books_string = '\n'.join(output_data)

    return all_books_string


def sort_list_by_author():
    """
    Sorts the book list alphabetically by author
    :return:
    """
    global book_list

    # This should in-place sort by the Book.author field
    book_list.sort(key=lambda x: x.author)

    # TODO trap if sort fails? Return True if it succeeds?


def sort_list_by_title():
    """
    Sorts the book list alphabetically by title
    :return:
    """
    global book_list

    book_list.sort(key=lambda x: x.title)


def sort_list_by_id():
    """
    Sorts the book list alphabetically by id
    :return:
    """
    global book_list

    book_list.sort(key=lambda x: x.book_id)
