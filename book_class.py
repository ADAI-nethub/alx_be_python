# book_class.py

class Book:
    """
    A class to represent a book with title, author, and publication year.
    It demonstrates Python magic methods for initialization, deletion,
    string representation, and official representation.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor method to initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.") # Optional: confirm creation

    def __del__(self):
        """
        Destructor method, called when the Book object is about to be destroyed.
        Prints a message indicating which book is being deleted.
        """
        # Ensure that the title attribute exists before trying to access it,
        # as __del__ can sometimes be called during unexpected cleanup
        # where attributes might no longer be available.
        if hasattr(self, 'title'):
            print(f"Deleting {self.title}")
        else:
            print("Deleting a Book object (title unknown).")

    def __str__(self):
        """
        Returns the user-friendly string representation of the Book object.
        This is what is displayed by `print()`.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns the official string representation of the Book object.
        This string should ideally be able to recreate the object.
        This is what is displayed by `repr()` or when the object is
        displayed in a collection (e.g., a list) without `print()`.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
