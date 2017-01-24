import os
import json
import datastore
from book import Book

# separator = '^^^'


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
            temp_list.extend(datastore.make_list(data))
    except FileNotFoundError:
        # First time program has run. Assume no books.
        pass
    return temp_list


def read_file_int(file_name, book_list):
    '''Read counter information from books'''
    try:
        with open(file_name) as f:
            try:
                counter = int(f.read())
            except IOError:
                counter = 0
    except IOError:
        counter = len(book_list)
    return counter


def check_dir(data_dir):
    '''Check data directory'''
    try:
        os.mkdir(data_dir)
    except FileExistsError:
        pass
