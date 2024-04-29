"""Module to check the function of construcot
    """
import random


class BankAccount:
    """
    Class to reparesent bankaccount

    """

    def __init__(self, account_number, balance, account_type):
        print("Constructor for bankaccount")
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        """
        Destructor
        """
        print("BackAccount Object Deleted")


class Customer:
    """
    Class to represent customers
    """

    def __init__(self, name, age, address, account_type) -> None:
        print("Constructor for customer")
        self.name = name
        self.age = age
        self.address = address
        self.account = BankAccount(random.randrange(
            200, 300), random.randrange(200, 300), account_type)

    def __del__(self):
        print("Customer object deleted")


customer = Customer("Sachin", 23, "Pepsicola", "savings")
