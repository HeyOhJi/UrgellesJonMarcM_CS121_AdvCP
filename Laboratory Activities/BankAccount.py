from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    @property
    def account_number(self):
        """Read-only access to account_number"""
        return self.__account_number

    @property
    def balance(self):
        """Read-only access to balance"""
        return self.__balance

    def _update_balance(self, amount):
        """Protected method to update balance"""
        self.__balance += amount

    @abstractmethod
    def deposit(self, amount):
        """Abstract method for depositing money"""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Abstract method for withdrawing money"""
        pass

    @abstractmethod
    def display_account_type(self):
        """Abstract method to display the account type"""
        pass


class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = -5000

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._update_balance(amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < self.OVERDRAFT_LIMIT:
            raise ValueError("Withdrawal exceeds overdraft limit.")
        self._update_balance(-amount)

    def display_account_type(self):
        return "Current Account"


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._update_balance(amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < 0:
            raise ValueError("Insufficient balance.")
        self._update_balance(-amount)

    def display_account_type(self):
        return "Savings Account"


def print_account_details(account):
    """Prints details of any BankAccount object"""
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(f"Account Type: {account.display_account_type()}")
    print("-" * 30)


# Testing the implementation
if __name__ == "__main__":
    # Create accounts
    savings1 = SavingsAccount("SAV123", 1000)
    savings2 = SavingsAccount("SAV456", 2000)
    current1 = CurrentAccount("CUR123", 500)
    current2 = CurrentAccount("CUR456", 1000)

    # Perform operations
    savings1.deposit(500)
    savings2.withdraw(1000)
    current1.deposit(1000)
    try:
        current2.withdraw(7000)  # Exceeds overdraft limit
    except ValueError as e:
        print(e)

    # Display account details
    print_account_details(savings1)
    print_account_details(savings2)
    print_account_details(current1)
    print_account_details(current2)