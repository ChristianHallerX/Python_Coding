"""
2043. Simple Bank System (medium)

You have been tasked with writing a program for a popular bank that will automate all its incoming transactions
(transfer, deposit, and withdraw).
The bank has n accounts numbered from 1 to n.
The initial balance of each account is stored in a 0-indexed integer array balance, with the (i + 1)th account having an initial balance of balance[i].

Execute all the valid transactions. A transaction is valid if:

- The given account number(s) are between 1 and n, and
- The amount of money withdrawn or transferred from is less than or equal to the balance of the account.

Implement the Bank class:

- Bank(balance: list[int]) Initializes the object with the 0-indexed integer array balance.

- boolean transfer(account1: int, account2: int, money: int)
    Transfers 'money' dollars from the account numbered  'account1' to the account numbered 'account2'.
    Return True if the transaction was successful, False otherwise.

- boolean deposit(account: int, money: int)
    Deposit 'money' dollars into the account numbered 'account'.
    Return True if the transaction was successful, False otherwise.

- boolean withdraw(account: int, money: int)
    Withdraw money dollars from the account numbered 'account'.
    Return True if the transaction was successful, False otherwise.
"""


class Bank:

    # instantiate bank with an amount for each account
    def __init__(self, balance: list[int]):
        self.balance = balance

    # transfer money from account 1 to account 2
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # check if both account numbers are valid and account1 has enough balance
        if (
            1 <= account1 <= len(self.balance)
            and 1 <= account2 <= len(self.balance)
            and self.balance[account1 - 1] >= money
        ):
            # deduct money from account1
            self.balance[account1 - 1] -= money
            # Add money to account2
            self.balance[account2 - 1] += money

            # Return True indicating the transfer was successful
            return True
        # if clause did not succeed
        return False

    # deposit money into a specific account
    def deposit(self, account: int, money: int) -> bool:
        # check if account number is valid
        if 1 <= account <= len(self.balance):
            # Add money
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        # check if account number is valid and sufficient money
        if 1 <= account <= len(self.balance) and self.balance[account - 1] >= money:
            # deduct money
            self.balance[account - 1] -= money
            return True
        return False


def main():
    balance = [10, 100, 20, 50, 30]
    obj = Bank(balance)
    param_1 = obj.withdraw(account=3, money=10)
    print(param_1, "expected: True")
    param_2 = obj.transfer(account1=5, account2=1, money=20)
    print(param_2, "expected: True")
    param_3 = obj.deposit(account=5, money=20)
    print(param_3, "expected: True")
    param_4 = obj.transfer(account1=3, account2=4, money=15)
    print(param_4, "expected: False")
    param_5 = obj.withdraw(account=10, money=50)
    print(param_5, "expected: False")


if __name__ == "__main__":
    main()
