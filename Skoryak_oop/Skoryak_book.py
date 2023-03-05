class Book:
    def __init__(self, name, author, year_publication):
        self.name = name
        self.author = author
        self.year_publication = year_publication

    def get_data_book(self):
        print(f'\n\tName: {self.name}   Author: {self.author}   Year of publication: {self.year_publication}\n')

    def get_data_age(self):
        try:
            if self.year_publication <= 0:
                raise ValueError
            print(f'\tThis book is {2023 - self.year_publication} years old\n')
        except ValueError:
            print('Incorrect year of publication\n')
        except TypeError:
            print('Use only numbers for year of publication\n')

some_book = Book("Harry Potter and the Philosopher's Stone", 'J. K. Rowling', 1997)
some_book.get_data_book()
some_book.get_data_age()