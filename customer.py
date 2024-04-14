# File:         book.py
# Author:       Nguyen Mia & Vo Thanh Anh Vu
# Description:  Classes related to customers

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.email} - {self.address}"

class CustomerManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def find_customer_by_name(self, name):
        # Find a customer by name in the customers list
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None
    
    def display_customers(self):
        print("\nCustomer List:")
        for customer in self.customers:
            print(customer)
