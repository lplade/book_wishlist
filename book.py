import datetime

class Book:
    """ Represents one book in a user's list of books"""

    NO_ID = -1
    NO_DATE = datetime.date(1970, 1, 1)  # this date means uninitialized

    def __init__(self, title, author, read=False,
                 book_id=NO_ID, date_read=NO_DATE):
        """
        Default book is unread, and has no ID
        """
        self.title = title
        self.author = author
        self.read = read
        self.id = book_id
        self.date_read = date_read

    def set_id(self, book_id):
        self.id = book_id

    def set_date_read(self, date_read=NO_DATE):
        if date_read == (1970, 1, 1):
            date_read = datetime.date.today()
        else:
            # TODO validate a passed date to be in datetime.date format
            # not used at this point
            pass
        self.date_read = date_read

    def __str__(self):
        read_str = 'no'
        if self.read:
            read_year = self.date_read.year()
            read_month = self.date_read.month()
            read_day = self.date_read.day()
            template = "{}-{}-{}"
            read_str = template.format(read_year, read_month, read_day)

        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        template = 'id: {} Title: {} Author: {} Read: {}'
        return template.format(id_str, self.title, self.author, read_str)

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and \
               self.read == other.read and self.id == other.id
