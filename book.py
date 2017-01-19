class Book:

    ''' Represents one book in a user's list of books'''

    NO_ID = -1
    NO_DATE = -1

    def __init__(self, title, author, read=False, book_id=NO_ID, date_read=NO_DATE):
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
        import datetime
        if date_read == -1:
            date = datetime.datetime.now()
        else:
            # TODO validate a passed date to be in datetime format
            # not used at this point
            pass
        self.date_read = date_read

    def __str__(self):
        read_str = 'no'
        if self.read:
            read_str = 'yes'

        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        template = 'id: {} Title: {} Author: {} Read: {}'
        return template.format(id_str, self.title, self.author, read_str)

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.read == other.read and self.id==other.id
