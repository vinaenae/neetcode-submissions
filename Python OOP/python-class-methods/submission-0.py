class Library:
    books_available = 100    # Total books in library

    @classmethod
    def lend_books(cls, val):
        cls.books_available -= val
    
    @classmethod
    def return_books(cls, num):
        cls.books_available += num
    # TODO: Implement class methods to manage book lending
    # TODO: Implement return_books method to increase the number of books available



# Don't change the code below
print(f"Initial status: {Library.books_available} books available")
Library.lend_books(30)
print(f"After lending: {Library.books_available} books available")
Library.return_books(10)
print(f"After return: {Library.books_available} books available")
