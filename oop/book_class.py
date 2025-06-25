# book_class.py

class Book:
    def __init__(self, title, author, year):
        """
        Constructor: Initializes a Book instance with title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor: Called when the Book object is about to be destroyed.
        """
        print(f"Deleting '{self.title}'")

    def __str__(self):
        """
        String representation: User-friendly description of the book.
        """
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation: Returns a string to recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage
if __name__ == "__main__":
    # Create a Book instance
    book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

    # Print the string and repr representations
    print(str(book1))    # Output: 'To Kill a Mockingbird' by Harper Lee, published in 1960
    print(repr(book1))   # Output: Book('To Kill a Mockingbird', 'Harper Lee', 1960)

    # Delete the object
    del book1            # Output: Deleting 'To Kill a Mockingbird'
