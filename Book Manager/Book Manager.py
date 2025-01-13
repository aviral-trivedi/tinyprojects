import json
import os


class Book:
    def __init__(self, title, author, category, isbn):
        self.title = str(title)
        self.author = str(author)
        self.category = str(category)
        self.isbn = isbn
        self.is_borrowed = False
        curator.add_book(self.title, self.author, self.category, self.isbn, self.is_borrowed)

    def __str__(self):
        return (f"Title:\t\t{self.title}\nAuthor:\t\t{self.author}\nCategory:\t{self.category}\nISBN:\t\t{self.isbn}\nBorrowed:\t{self.is_borrowed}\n")

class BookManager:
    def __init__(self):
        self.book_list = {}
        
    def add_book(self, title, author, category, isbn, borrowed):
        if category not in self.book_list:
            self.book_list[category] = {}
            print(f"Created Category '{category}'")
            self.book_list[category][title] = {
                'author': author,
                'isbn': isbn,
                'borrowed': borrowed
                }
            print(f"'{title}' Added to {category}")
            print()
        else:
            self.book_list[category][title] = {
                'author': author,
                'isbn': isbn,
                'borrowed': borrowed}
            print(f"'{title}' Added to {category}")
            print()
        
    def remove_book(self, title, category, isbn):
        if category not in self.book_list:
            print("Category Not Found")
            return
        elif title and isbn not in self.book_list:
            print("Title or ISBN Not Found")
            return
        else:
            del self.book_list[category][title]
            if len(self.book_list[category])==0:
                del self.book_list[category]

    def list_books(self):
        for category in self.book_list:
            print(f"{category}:")
            for title in self.book_list[category]:
              print(f"\t'{title}': {self.book_list[category][title]}")

    def is_available(self, isbn):
        for category in self.book_list:
            for title in self.book_list[category]:
                for key, value in self.book_list[category][title].items():
                    if key == 'isbn' and value == isbn:
                        if self.book_list[category][title]['borrowed'] != False:
                            print("Available but borrowed.")
                    else:
                        print("Not available")

    def borrow(self, isbn):
        for category in self.book_list:
            for title in self.book_list[category]:
                for key, value in self.book_list[category][title].items():
                    if key == 'isbn' and value == isbn:
                        if self.book_list[category][title]['borrowed'] != False:
                            print("Book is already borrowed.")
                        else:
                            self.book_list[category][title]['borrowed'] = True
                            print(f"The book {list(self.book_list[category].keys())[0]} is borrowed = {self.book_list[category][title]['borrowed']}") 

    def return_book(self, isbn):
        for category in self.book_list:
            for title in self.book_list[category]:
                for key, value in self.book_list[category][title].items():
                    if key == 'isbn' and value == isbn:
                        self.book_list[category][title]['borrowed'] = False
                        print(f"The book {list(self.book_list[category].keys())[0]} is borrowed = {self.book_list[category][title]['borrowed']}") 

curator = BookManager()


#murder = Book("Murder!", "Arnold Bennett", "Crime", "1-86092-012-8")
#occurrence = Book("An Occurrence at Owl Creek Bridge One of the Missing", "Ambrose Bierce", "Adventure", "1-86092-006-3")

#curator.borrow("1-86092-012-8")
#curator.borrow("1-86092-012-8")
