def read_file(file_name):
    temp_list = []
    try:
        with open(file_name, 'r') as f:
            data = f.read()
            temp_list.append(make_list(data))
    return temp_list

def read_file_int(file_name):
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
    try:
        os.mkdir(data_dir)
    except FileExistsError:
        pass

def make_list(string_from_file):
    temp_list = []
    books_str = string_from_file.split('\n')

    for book_str in books_str:
        data = book_str.split(separator)
        book = Book(data[0], data[1], data[2] == 'True', int(data[3]))
        temp_list.append(book)
    return temp_list
