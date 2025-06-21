from library_system import Book, EBook, PrintBook, Library

def test_book_initialization():
    """Test Book class initialization."""
    book = Book("Test Title", "Test Author")
    print(f"Book initialized: {book.title}, {book.author}")
    print(f"Book __str__: {book}")
    print()

def test_ebook_initialization():
    """Test EBook class initialization."""
    ebook = EBook("Test EBook", "Test EBook Author", 1024)
    print(f"EBook initialized: {ebook.title}, {ebook.author}, {ebook.file_size}")
    print(f"EBook __str__: {ebook}")
    print()

def test_printbook_initialization():
    """Test PrintBook class initialization."""
    printbook = PrintBook("Test PrintBook", "Test PrintBook Author", 300)
    print(f"PrintBook initialized: {printbook.title}, {printbook.author}, {printbook.page_count}")
    print(f"PrintBook __str__: {printbook}")
    print()

def test_library_initialization():
    """Test Library class initialization."""
    library = Library()
    print(f"Library initialized with {len(library.books)} books")
    print()

if __name__ == "__main__":
    print("Testing class initialization...")
    print("=" * 50)
    test_book_initialization()
    test_ebook_initialization()
    test_printbook_initialization()
    test_library_initialization()
    print("All classes initialized successfully!")

