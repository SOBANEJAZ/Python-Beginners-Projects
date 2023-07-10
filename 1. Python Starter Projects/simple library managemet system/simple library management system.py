class library:
    number_of_books = 0

    def __init__(self):
        self.name_of_books = []
        

    def add_book(self, books):
        self.name_of_books.append(books)
        library.number_of_books += 1

    def print_info(self):
        print(f"There are total of {self.number_of_books} books and the books are ")
        for i in self.name_of_books:
            print(i)


my_library = library()
my_library.add_book("A little life")
my_library.add_book("The book theif")
my_library.add_book("kite runner")
my_library.add_book("A Thousand splendid suns")
my_library.print_info()
