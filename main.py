from customer import Customer, CustomerManager
from book import Book, FictionBook, NonFictionBook
from inventory import Inventory
from order import OrderProcessor


def main():
    # Create an OrderProcessor instance
    processor = OrderProcessor()

    # Add customers to the customer manager
    processor.customer_manager.add_customer("John", "john@email.com", "123 Victoria St")
    processor.customer_manager.add_customer("Paul", "paul@email.com", "456 Queen St")

    # Display customer list
    processor.customer_manager.display_customers()

    # Add books to the inventory
    processor.inventory.add_book_to_inventory("Summer Fridays", "Suzanne Rindell", 24.99, "Fiction", "Fantasy", 8)
    processor.inventory.add_book_to_inventory("The Morningside", "Tea Obreht", 13.99, "Fiction", "Romance", 10)
    processor.inventory.add_book_to_inventory("Becoming", "Michelle Obama", 12.99, "Non-Fiction", "Education", 5)

    # Display current inventory
    processor.inventory.display_inventory()

    # Process order 1
    try:
        order1 = processor.process_order("Paul", [("Summer Fridays", 2), ("Becoming", 5)], "express")
        print("\nOrder 1 Details:")
        print(order1)        
    except ValueError as e:
        print(f"\nError processing order 1: {e}")

    # Process order 2
    try:
        order2 = processor.process_order("John", [("The Morningside", 1), ("Becoming", 2)], "standard")
        print("\nOrder 2 Details:")
        print(order2)
    except ValueError as e:
        print(f"\nError processing order 2: {e}")

    # Display current inventory
    processor.inventory.display_inventory()


if __name__ == "__main__":
    main()
