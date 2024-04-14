# File:         book.py
# Author:       Nguyen Mia & Vo Thanh Anh Vu
# Description:  Classes representing different types of books

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        # Return the string representation of the book.
        return f"{self.title} by {self.author} - ${self.price}"


class FictionBook(Book):
    def __init__(self, title, author, price, genre):
        super().__init__(title, author, price)
        self.genre = genre  

    def __str__(self):
        # Return the string representation of the fiction book, including its genre.
        return f"Fiction: {super().__str__()} - Genre: {self.genre}"


class NonFictionBook(Book):
    def __init__(self, title, author, price, subject):
        super().__init__(title, author, price)
        self.subject = subject  

    def __str__(self):
        # Return the string representation of the non-fiction book, including its subject.
        return f"Non-Fiction: {super().__str__()} - Subject: {self.subject}"
