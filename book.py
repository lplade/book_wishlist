class Book:

    ''' Represents one book in a user's list of books'''

    NO_ID = -1
    UNRATED = -1

    def __init__(self, title, author, read=False, id=NO_ID, rating=UNRATED):
        '''Default book is unread, and has no ID'''
        self.title = title
        self.author = author
        self.read = read
        self.id=id
        self.rating=rating


    def set_id(self, id):
        self.id = id


    def __str__(self):
        read_str = 'no'
        if self.read:
            read_str = 'yes'

        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        rating_str = self.rating
        if self.rating == -1:
            rating_str = 'Not Rated'

        template = 'id: {} Title: {} Author: {} Read: {} Rating: {}'
        return template.format(id_str, self.title, self.author, read_str, rating_str)


    def __eq__(self, other):
        return ((self.title, self.author, self.read, self.id) == \
                (other.title,other.author,other.read,other.id))
        #return self.title == other.title and self.author == other.author and self.read == other.read and self.id==other.id
