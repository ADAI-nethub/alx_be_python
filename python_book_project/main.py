# main.py
# This script is used to test the Book class defined in book_class.py.

# Import the Book class from the book_class module
from book_class import Book

def main():
    """
    Main function to demonstrate the functionality of the Book class,
    including its constructor, string representation, official representation,
    and destructor.
    """
    # Creating an instance of Book
    # This will call the __init__ method.
    my_book = Book("1984", "George Orwell", 1949)

    print("\n--- Demonstrating __str__ method ---")
    # Demonstrating the __str__ method
    # When print() is called on an object, Python looks for the __str__ method.
    print(my_book)  # Expected to use __str__

    print("\n--- Demonstrating __repr__ method ---")
    # Demonstrating the __repr__ method
    # The repr() function explicitly calls the __repr__ method.
    print(repr(my_book))  # Expected to use __repr__

    print("\n--- Demonstrating __del__ method ---")
    # Deleting a book instance to trigger __del__
    # The __del__ method is called when the object's reference count drops to zero.
    # This explicit 'del' statement removes the last reference, triggering __del__.
    del my_book
    
    # Note: Sometimes there can be a slight delay before __del__ is called
    # if there are other lingering references or garbage collection schedules.
    # In simple scripts like this, 'del' usually triggers it immediately.
    print("Program finished. __del__ should have been called.")

if __name__ == "__main__":
    # Ensure the main function is called only when the script is executed directly.
    main()

