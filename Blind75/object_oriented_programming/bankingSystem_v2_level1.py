"""
Banking System (4-level CodeSignal problem)

Level 1: Implement three basic methods:
    - deposit(account, amount): Add money to a valid account.
    - withdraw(account, amount): Withdraw money (only if the account exists and has enough funds).
    - transfer(src, target, amount): Withdraw money from the source and deposit into the target if possible.

Level 2: Track a transaction counter for every account
    (each successful deposit, withdrawal, or transfer increases the counter) and implement a method to
    return the top 'n' accounts with the most transactions.

Level 3: Add a pending transfer system:
    - initiate_transfer(src, target, timestamp, amount): This “withholds” (deducts) money from the source
        account and returns a transfer string (like "Transfer1", "Transfer2", …).
    - accept_transfer(transfer_str, acceptance_timestamp): This allows the target account to “accept”
        the pending money only if it is accepted within 24 hours (i.e. 86400 seconds) from the original
        timestamp. If accepted, the money is deposited into the target account.

Level 4: unknown ????
"""


#### Level 1: Basic Banking Operations ####
class Bank:
    def __init__(self, balance):
        # Accounts are 1-indexed; store balances in a list.
        self.accounts = balance[:]  # Make a copy of the initial balances.

    def deposit(self, account, amount):
        """Deposits 'amount' into 'account'. Returns True if successful, else False."""
        if account < 1 or account > len(self.accounts):
            return False
        self.accounts[account - 1] += amount
        return True

    def withdraw(self, account, amount):
        """Withdraws 'amount' from 'account'. Returns True if successful, else False."""
        if (
            account < 1
            or account > len(self.accounts)
            or self.accounts[account - 1] < amount
        ):
            return False
        self.accounts[account - 1] -= amount
        return True

    def transfer(self, src, target, amount):
        """
        Transfers 'amount' from src to target.
        Returns True if successful (valid accounts and sufficient funds), else False.
        """
        if (
            src < 1
            or src > len(self.accounts)
            or target < 1
            or target > len(self.accounts)
            or self.accounts[src - 1] < amount
        ):
            return False

        self.accounts[src - 1] -= amount
        self.accounts[target - 1] += amount
        return True


# Example usage:
if __name__ == "__main__":
    bank = Bank([100, 200, 300])
    print(bank.deposit(1, 50))  # Should print True; account 1 becomes 150.
    print(bank.withdraw(2, 100))  # Should print True; account 2 becomes 100.
    print(
        bank.transfer(3, 1, 150)
    )  # Should print True; account 3 becomes 150, account 1 becomes 300.
