# programming_paradigm/library_management.py

class Book:
    """
    Represents a book in the library with a title, author,
    and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Marks the book as checked out if it's available.
        Returns True if successful, False otherwise (already checked out).
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as available if it's checked out.
        Returns True if successful, False otherwise (already available).
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Checks if the book is currently available.
        Returns True if available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book instances, allowing adding, checking out,
    returning, and listing available books.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if not isinstance(book, Book):
            print("Error: Only Book objects can be added to the library.")
            return
        self._books.append(book)
        # No print statement here as the example output doesn't show "Added..." for new books.

    def check_out_book(self, title):
        """
        Attempts to check out a book by its title.

        Args:
            title (str): The title of the book to check out.
        Returns:
            Book: The checked-out Book object if successful, None otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    # print(f"Checked out '{book.title}'.") # Remove print for exact output matching
                    return book
                else:
                    # print(f"'{book.title}' is already checked out.") # Remove print for exact output matching
                    return None # Book found but already checked out
        # print(f"Error: Book '{title}' not found in the library.") # Remove print for exact output matching
        return None # Book not found

    def return_book(self, title):
        """
        Attempts to return a book by its title.

        Args:
            title (str): The title of the book to return.
        Returns:
            Book: The returned Book object if successful, None otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    # print(f"Returned '{book.title}'.") # Remove print for exact output matching
                    return book
                else:
                    # print(f"'{book.title}' was not checked out.") # Remove print for exact output matching
                    return None # Book found but not checked out
        # print(f"Error: Book '{title}' not found in the library.") # Remove print for exact output matching
        return None # Book not found

    def list_available_books(self):
        """
        Lists all books currently available in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available.")
            return

        for book in available_books:
            print(book) # Uses the __str__ method of the Book class