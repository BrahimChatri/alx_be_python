class Book:
    """Base class representing a book."""
    
    def __init__(self, title, author):
        """Initialize book with title and author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    
    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """String representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""
    
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """String representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library class demonstrating composition by managing a collection of books."""
    
    def __init__(self):
        """Initialize library with an empty books list."""
        self.books = []
    
    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)
    
    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)

