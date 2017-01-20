import os
from book import Book

separator = '^^^'

def write_file(file_name, data):
    '''Write passed data to file'''
    with open(file_name, 'w') as f:
        f.write(data)


def read_file(file_name):
    '''Read lines from wishlist.txt'''
    temp_list = []
    try:
        with open(file_name) as f:
            data = f.read()
            temp_list.extend(make_list(data))
    except FileExistsError:
        pass
    return temp_list

def read_file_int(file_name, book_list):
    '''Read counter information from books'''
    try:
        with open(file_name) as f:
            try:
                counter = int(f.read())
            except:
                counter = 0
    except:
        counter = len(book_list)
    return counter

def check_dir(data_dir):
    '''Check data directory'''
    try:
        os.mkdir(data_dir)
    except FileExistsError:
        pass

def make_list(string_from_file):
    '''Creates list to return to read_file function'''
    temp_list = []
    books_str = string_from_file.split('\n')

    for book_str in books_str:
        data = book_str.split(separator)
        book = Book(data[0], data[1], data[2] == 'True', int(data[3]))
        temp_list.append(book)
    return temp_list
