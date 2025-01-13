import json
import os

def json_file_exists(filename):    
    # Get the directory of the current Python file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the file
    file_path = os.path.join(current_directory, filename)
    # Check if the file exists
    if not os.path.exists(file_path):
        # Create the file
        with open(file_path, 'w') as file:
            pass

class Book:
    """A class representing a book."""

    def __init__(self, title, author, category, isbn):
        """Initialize a new book.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            category (str): The category of the book.
            isbn (str): The ISBN number of the book.
        """
        self.title = str(title)
        self.author = str(author)
        self.category = str(category)
        self.isbn = isbn
        self.is_borrowed = False
        curator.add_book(self.title, self.author, self.category, self.isbn, self.is_borrowed)
        
    def __str__(self):
        """Return a string representation of the book."""
        return (f"Title:\t\t{self.title}\n"
                f"Author:\t\t{self.author}\n"
                f"Category:\t{self.category}\n"
                f"ISBN:\t\t{self.isbn}\n"
                f"Borrowed:\t{self.is_borrowed}\n")

class Curator:
    """A class representing a curator of a library."""

    def __init__(self):
        """Initialize a new curator."""
        self.book_list = {}

    def add_book(self, title, author, category, isbn, borrowed):
        """Add a new book to the library.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            category (str): The category of the book.
            isbn (str): The ISBN number of the book.
            borrowed (bool): Whether the book is borrowed or not.
        """
        category = category.lower()
        if category not in self.book_list:
            self.book_list[category] = {}
            print(f"Created Category '{category}'")
        if title in self.book_list[category]:
            print(f"'{title}' already exists in {category}")
        else:
            self.book_list[category][title] = {
                'author': author,
                'isbn': isbn,
                'borrowed': borrowed
                }
            print(f"'{title}' Added to {category}")
            print()

    def remove_book(self, title, category, isbn):
        """Remove a book from the library.

        Args:
            title (str): The title of the book.
            category (str): The category of the book.
            isbn (str): The ISBN number of the book.
        """
        category = category.lower()
        if category not in self.book_list:
            print("Category Not Found")
            return
        if title not in self.book_list[category]:
            print("Title Not Found")
            return
        if self.book_list[category][title]['isbn'] != isbn:
            print("ISBN Mismatch")
            return
        del self.book_list[category][title]
        if len(self.book_list[category])==0:
            del self.book_list[category]

    def list_books(self):
        """List all books in the library."""
        for category in self.book_list:
            print(f"{category}:")
            for title in self.book_list[category]:
                print(f"\t'{title}': {self.book_list[category][title]}")

    def is_available(self, isbn):
        """Check if a book is available.

        Args:
            isbn (str): The ISBN number of the book.
        """
        for category in self.book_list:
            for title in self.book_list[category]:
                if self.book_list[category][title]['isbn'] == isbn and not self.book_list[category][title]['borrowed']:
                    print("Available")
                    return
        print("Not available")

    def borrow(self, isbn):
        """Borrow a book.

        Args:
            isbn (str): The ISBN number of the book.
        """
        for category in self.book_list:
            for title in self.book_list[category]:
                if self.book_list[category][title]['isbn'] == isbn and not self.book_list[category][title]['borrowed']:
                    self.book_list[category][title]['borrowed'] = True
                    print(f"The book {title} is borrowed = {self.book_list[category][title]['borrowed']}")
                    return
        print("Book not found or already borrowed")

    def return_book(self, isbn):
        """Return a book.

        Args:
            isbn (str): The ISBN number of the book.
        """
        for category in self.book_list:
            for title in self.book_list[category]:
                if self.book_list[category][title]['isbn'] == isbn:
                    self.book_list[category][title]['borrowed'] = False
                    print(f"The book {title} is borrowed = {self.book_list[category][title]['borrowed']}")
                    return
        print("Book not found")

    def save_books(self, filename="Books"):
        """Save the book list to a JSON file.

        Args:
            filename (str): The name of the JSON file.
        """
        with open(filename, 'a') as f:
            json.dump(self.book_list, f, indent=4)

    def load_books(self, filename="Books"):
        """Load the book list from a JSON file.

        Args:
            filename (str): The name of the JSON file.
        """
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.book_list = json.load(f)
        else:
            print("File not found")

curator = Curator()
json_file_exists("Books")

# murder = Book("Murder!", "Arnold Bennett", "Crime", "1-86092-012-8")
# occurrence = Book("An Occurrence at Owl Creek Bridge One of the Missing", "Ambrose Bierce", "Adventure", "1-86092-006-3")



