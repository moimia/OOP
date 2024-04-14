# File:         inventory.py
# Author:       Nguyen Mia & Vo Thanh Anh Vu
# Description:  Inventory class represents the inventory of books and 
#               allows for adding books, checking the availability, and updating the stock quantity

from book import Book, FictionBook, NonFictionBook

class Inventory:
    def __init__(self):
        self.books_in_stock = {}

    def add_book_to_inventory(self, title, author, price, book_type=None, genre_or_subject=None, quantity=1):
        # Add a new book to the inventory based on its type
        if book_type == "Fiction":
            book = FictionBook(title, author, price, genre_or_subject)
        elif book_type == "Non-Fiction":
            book = NonFictionBook(title, author, price, genre_or_subject)
        else:
            book = Book(title, author, price)
        self.books_in_stock[title] = {'book': book, 'quantity': quantity}

    def find_book_by_title(self, title):
        if title in self.books_in_stock:
            return self.books_in_stock[title]['book']
        return None

    def check_stock_availability(self, title, quantity):
        book_info = self.books_in_stock.get(title)
        if book_info and book_info['quantity'] >= quantity:
            return True
        return False

    def update_stock(self, title, quantity):
        book_info = self.books_in_stock.get(title)
        if book_info:
            book_info['quantity'] -= quantity
            return True
        return False
    
    def display_inventory(self):
        print("\nCurrent Inventory:")
        for title, info in self.books_in_stock.items():
            book = info['book']
            quantity = info['quantity']
            print(f"{book} - Quantity in stock: {quantity}")
