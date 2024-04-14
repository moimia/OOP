# File:         order.py
# Author:       Nguyen Mia & Vo Thanh Anh Vu
# Description:  The Order class represents an order placed by a customer & the OrderProcessor class handles the processing of orders

from customer import CustomerManager
from inventory import Inventory

class Order:
    def __init__(self, customer, items, shipping_method, inventory):
        self.customer = customer
        self.items = items
        self.shipping_method = shipping_method
        self.inventory = inventory

    def calculate_total(self):
        total = sum(self.inventory.find_book_by_title(item[0]).price * item[1] for item in self.items)
        if self.shipping_method == 'express':
            total += 10  # Express shipping fee
        return total      

    def __str__(self):
        book_list = '\n'.join([
            f"{book} - Quantity: {quantity}, Price: ${self.inventory.find_book_by_title(book).price}"
            for book, quantity in self.items
        ])
        shipping_cost = 10 if self.shipping_method == 'express' else 0
        total_cost = self.calculate_total()
        return f"Customer: {self.customer} \n{book_list}\nShipping Method: {self.shipping_method} (+${shipping_cost})\nTotal: ${total_cost}"


class OrderProcessor:
    def __init__(self):
        self.inventory = Inventory()
        self.customer_manager = CustomerManager()

    def process_order(self, customer_name, items, shipping_method):
        # Find the customer by name
        customer = self.customer_manager.find_customer_by_name(customer_name)
        if customer is None:
            # If customer is not found, raise an exception
            raise ValueError("Customer not found.")

        # Check if items are available in inventory
        for item in items:
            # Check if the item exists
            if not self.inventory.find_book_by_title(item[0]):
                raise ValueError(f"Item '{item[0]}' does not exist.")
            
            # Check if there is enough stock available for the item
            if not self.inventory.check_stock_availability(item[0], item[1]):
                raise ValueError(f"Not enough stock available for '{item[0]}'.")

        # Create the order
        order = Order(customer, items, shipping_method, self.inventory)

        # Update the stock
        for item in items:
            self.inventory.update_stock(item[0], item[1])

        total = order.calculate_total()
        return order
