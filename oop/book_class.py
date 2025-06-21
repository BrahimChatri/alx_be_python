class Book:
    """A class representing a book with magic methods."""
    
    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor that prints a message when the book is deleted."""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """String representation for user-friendly output."""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Official representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

