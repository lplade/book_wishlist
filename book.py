import datetime
import json
from time import mktime


class Book:
    """ Represents one book in a user's list of books"""

    NO_ID = -1
    NO_DATE = 0  # this date means uninitialized
    UNRATED = -1

    def __init__(self, title, author, read=False,
                 book_id=NO_ID, date_read=NO_DATE, rating=UNRATED):
        """
        Default book is unread, and has no ID
        """
        self.title = title
        self.author = author
        self.read = read
        self.book_id = book_id
        self.date_read = date_read
        self.rating = rating

    # http://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
    @classmethod
    def from_json(cls, json_string):
        """
        use this alternate "constructor" when we're parsing the stored data
        :param json_string:
        :return:
        """
        parsed_json = json.loads(json_string)
        title = parsed_json["title"]
        author = parsed_json["author"]
        read = parsed_json["read"]
        book_id = parsed_json["book_id"]

        # date should be stored in ISO YYYY-MM-DD format,
        # parse it into a datetime.date object
        raw_date_read = parsed_json["date_read"]
        try:
            _yyyy, _mm, _dd = raw_date_read.split('-')
            date_read = datetime.date(_yyyy, _mm, _dd)
        except:  # Which exception? Trying to catch uninitialized case
            date_read = raw_date_read

        rating = parsed_json["rating"]

        # construct a new object based on these fields
        return cls(title, author, read, book_id, date_read, rating)

    def set_id(self, book_id):
        self.book_id = book_id

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

        id_str = self.book_id
        if self.book_id == -1:
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
        return (self.title, self.author, self.read, self.book_id) == \
               (other.title, other.author, other.read, other.id)

    def to_json(self):
        """
        This serializes contents of current object to json string
        :rtype: str
        :return:
        """
        # we need a special encoder to handle the datetime.date object
        return json.dumps(self, cls=_DTEncoder)


# Helper class

# Lifted from Introducing Python, p. 191
class _DTEncoder(json.JSONEncoder):
    def default(self, obj):
        # isinstance() checks the type of obj
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        # else it's something the normal decoder knows:
        # return json.JSONEncoder.default(self, obj)
        return obj.__dict__

