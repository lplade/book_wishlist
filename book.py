import datetime
import json
from time import mktime


class Book:
    """ Represents one book in a user's list of books"""

    NO_ID = -1
    NO_DATE = datetime.date(1970, 1, 1)  # this date means uninitialized
    UNRATED = -1

    def __init__(self, title, author, read=False,
                 book_id=NO_ID, date_read=NO_DATE, rating=UNRATED):
        """
        Default book is unread, and has no ID
        """
        self.title = title
        self.author = author
        self.read = read
        self.id = book_id
        self.date_read = date_read
        self.rating = rating

    def set_id(self, book_id):
        self.id = book_id

    def set_date_read(self, new_date_read=NO_DATE):
        if new_date_read == datetime.date(1970, 1, 1):
            new_date_read = datetime.date.today()
        else:
            # TODO validate this?
            pass
        self.date_read = new_date_read

    def __str__(self):
        read_str = 'no'
        # Display date read in 2016-12-31 format if read, otherwise display 'no'
        if self.read:
            # Native datetime str format happens to be the one we want!
            read_str = str(self.date_read)

        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        rating_str = self.rating
        if self.rating == -1:
            rating_str = 'Not Rated'

        template = 'id: {} Title: {} Author: {} Read: {} Rating: {}'
        return template.format(id_str, self.title, self.author,
                               read_str, rating_str)

    def __eq__(self, other):

        # return self.title == other.title and self.author == other.author and \
        #        self.read == other.read and self.id == other.id

        # why this change? -lpl
        return (self.title, self.author, self.read, self.id) == \
               (other.title, other.author, other.read, other.id)

    def to_json(self):
        """
        This serializes contents of current object to json string
        :rtype: str
        :return:
        """
        # we need a special encoder to handle the datetime.date object
        return json.dumps(self, cls=DTEncoder)


# Helper class
# Lifted from Introducing Python, p. 191
class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        # isinstance() checks the type of obj
        if isinstance(obj, datetime.date):
            return int(mktime(obj.timetuple()))  # should be epoch time
        # else it's something the normal decoder knows:
        return json.JSONEncoder.default(self, obj)



