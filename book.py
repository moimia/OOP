class Book:
    def __init__(self, title, author, price):
        # Initialize a new book instance with a title, an author, and a price.
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        # Return the string representation of the book.
        return f"{self.title} by {self.author} - ${self.price}"


class FictionBook(Book):
    def __init__(self, title, author, price, genre):
        # Initialize a new fiction book instance.
        # Calls the constructor of the base class (Book) to set title, author, and price.
        super().__init__(title, author, price)
        self.genre = genre  # Additional attribute for the genre of the book.

    def __str__(self):
        # Return the string representation of the fiction book, including its genre.
        return f"Fiction: {super().__str__()} - Genre: {self.genre}"


class NonFictionBook(Book):
    def __init__(self, title, author, price, subject):
        # Initialize a new non-fiction book instance.
        # Calls the constructor of the base class (Book) to set title, author, and price.
        super().__init__(title, author, price)
        self.subject = subject  # Additional attribute for the subject of the book.

    def __str__(self):
        # Return the string representation of the non-fiction book, including its subject.
        return f"Non-Fiction: {super().__str__()} - Subject: {self.subject}"
