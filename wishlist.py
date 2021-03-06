# Main program

import ui
import datastore
from book import Book


def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        check_duplicate_book()

    elif choice == '5':
        delete_book()

    elif choice == '6':
        modify_book()

    elif choice == '7':
        rate_book()

    elif choice == '8':
        search_books()

    elif choice == '9':
        change_sort_order()

    elif choice == 'q':
        quit_and_save()

    else:
        ui.message('Please enter a valid selection')


def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)


def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()
    date_read = ui.ask_for_date_read()
    if datastore.set_read(book_id, date_read, True):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def new_book(book_title, book_author):
    '''Add new book'''
    book = Book(book_title, book_author)
    datastore.add_book(book)
    ui.message('Book added: ' + str(book))


def check_duplicate_book():
    book_title, book_author = ui.get_book_info()
    if datastore.check_book(book_title, book_author):
        if ui.confirm_new_book():
            new_book(book_title, book_author)
        else:
            ui.message('Aborting operation.')
    else:
        new_book(book_title, book_author)


def modify_book():
    '''
    Get book ID from user, modify title/author
    '''
    book_id = ui.ask_for_book_id()
    book_title, book_author = ui.get_book_info()
    datastore.set_book_information(book_id, book_title, book_author)


def rate_book():
    '''Get book ID from user, set rating'''
    book_id = ui.ask_for_book_id()
    book_rating = ui.get_book_rating()
    datastore.set_book_rating(book_id, book_rating)


def search_books():
    book_title, book_author = ui.get_book_info()
    found_books = datastore.find_book(book_title, book_author)
    ui.show_list(found_books)


def delete_book():
    """
    Get book id from user, deletes book
    :return:
    """
    book_id = ui.ask_for_book_id()
    if datastore.delete_book(book_id):
        ui.message("Successfully deleted")
    else:
        ui.message("Book id not found in database")


def change_sort_order():
    """
    Prompt to change order books are stored in
    :return:
    """
    choice = ui.display_menu_sort_order()

    while True:  # loop until we get a valid number
        if choice == '1':
            datastore.sort_list_by_id()
        elif choice == '2':
            datastore.sort_list_by_author()
        elif choice == '3':
            datastore.sort_list_by_title()
        else:
            ui.message("Please make a valid choice")
            continue
        break


def quit_and_save():
    """Perform shutdown tasks"""
    datastore.shutdown()
    ui.message('Bye!')


def main():

    datastore.setup()

    _quit = 'q'
    choice = None

    while choice != _quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
