# Define the Book class
class Book:
    def _init_(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


# Define the Ebook class, a subclass of Book
class Ebook(Book):
    def _init_(self, title, author, isbn, file_format):
        super()._init_(title, author, isbn)
        self.file_format = file_format

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, File Format: {self.file_format}"


# Define the Library class
class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_all_books(self):
        return [book.display_info() for book in self.books]

    def search_book_by_title(self, title):
        result = [book.display_info() for book in self.books if book.title.lower() == title.lower()]
        return result


# Example usage
try:
    # Create instances of Book, Ebook, and Library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-3-16-148410-0")
    ebook1 = Ebook("Python Basics", "John Doe", "978-1-23-456789-0", "PDF")
    library = Library()

    # Add books to the library
    library.add_book(book1)
    library.add_book(ebook1)

    # Display all books in the library
    all_books = library.display_all_books()
    print("All Books in the Library:")
    for book_info in all_books:
        print(book_info)

    # Search for a book by title
    search_result = library.search_book_by_title("python basics")
    print("\nSearch Result:")
    for book_info in search_result:
        print(book_info)

except Exception as e:
    print(f"An error occurred: {e}")
