
import os
from book import Book
from file_io import *

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

separator = '^^^'  # a string probably not in any valid data relating to a book

book_list = []
counter = 0

def setup():
    ''' Read book info from file, if file exists. '''

    global counter, book_list

    book_list.append(read_file(BOOKS_FILE_NAME))
    counter = read_file_int(COUNTER_FILE_NAME, book_list)


def shutdown():
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''

    output_data = make_output_data()
    # Create data directory
    check_dir(DATA_DIR)
    write_file(BOOKS_FILE_NAME, output_data)
    write_file(COUNTER_FILE_NAME, str(counter))
    # with open(BOOKS_FILE_NAME, 'w') as f:
    #     f.write(output_data)
    #
    # with open(COUNTER_FILE_NAME, 'w') as f:
    #     f.write(str(counter))


def get_books(**kwargs):
    ''' Return books from data store. With no arguments, returns everything. '''

    global book_list

    if len(kwargs) == 0:
        return book_list

    if 'read' in kwargs:
        read_books = [ book for book in book_list if book.read == kwargs['read'] ]
        return read_books



def add_book(book):
    ''' Add to db, set id value, return Book'''

    global book_list

    book.id = generate_id()
    book_list.append(book)


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
        if book.id == book_id:
            book_list.remove(book)  # remove matching book from list
            return True

    return False  # return False if book id is not found


def set_read(book_id, read):
    '''Update book with given book_id to read. Return True if book is found in DB and update is made, False otherwise.'''

    global book_list

    for book in book_list:

        if book.id == book_id:
            book.read = True
            return True

    return False # return False if book id is not found


def make_output_data():
    ''' create a string containing all data on books, for writing to output file'''

    global book_list

    output_data = []

    for book in book_list:
        output = [ book.title, book.author, str(book.read), str(book.id) ]
        output_str = separator.join(output)
        output_data.append(output_str)

    all_books_string = '\n'.join(output_data)

    return all_books_string
