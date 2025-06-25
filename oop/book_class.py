#!/usr/bin/python3
"""
Defines a Book class for a simple book project.
"""

class Book:
    """
    Represents a book with a title, author, and publication year.
    """

    def __init__(self, title, author, year):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        if not isinstance(title, str) or not title:
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(author, str) or not author:
            raise ValueError("Author must be a non-empty string.")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer.")

        self.__title = title
        self.__author = author
        self.__year = year

    @property
    def title(self):
        """Gets the title of the book."""
        return self.__title

    @property
    def author(self):
        """Gets the author of the book."""
        return self.__author

    @property
    def year(self):
        """Gets the publication year of the book."""
        return self.__year

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        Matches the format: "TITLE by AUTHOR, published in YEAR"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an unambiguous string representation of the Book object,
        primarily for debugging.
        Matches the format: Book('TITLE', 'AUTHOR', YEAR)
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor for the Book object, called when the object is deleted.
        Prints a message indicating the deletion of the book by its title.
        """
        print(f"Deleting {self.title}")

if __name__ == "__main__":
    # Example usage within book_class.py for testing
    try:
        my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
        print(my_book) # Uses __str__
        print(repr(my_book)) # Uses __repr__

        another_book = Book("1984", "George Orwell", 1949)
        print(another_book)
        print(repr(another_book))

        del another_book # Calls __del__

    except ValueError as e:
        print(f"Error creating book: {e}")