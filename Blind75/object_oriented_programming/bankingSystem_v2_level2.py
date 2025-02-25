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


#### Level 2: Top N Accounts by Transaction Count ####
class Bank:
    def __init__(self, balance):
        self.accounts = balance[:]  # Copy initial balances.
        ###### NEW track the number of transactions per account with a list and int for each account
        self.transaction_counts = [0] * len(balance)

    def deposit(self, account, amount):
        if account < 1 or account > len(self.accounts):
            return False
        self.accounts[account - 1] += amount
        ###### NEW increment transaction count
        self.transaction_counts[account - 1] += 1
        return True

    def withdraw(self, account, amount):
        if (
            account < 1
            or account > len(self.accounts)
            or self.accounts[account - 1] < amount
        ):
            return False
        self.accounts[account - 1] -= amount
        ###### NEW increment transaction count
        self.transaction_counts[account - 1] += 1
        return True

    def transfer(self, src, target, amount):
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
        ####### NEW increment transaction count
        self.transaction_counts[src - 1] += 1
        self.transaction_counts[target - 1] += 1
        return True

    ###### NEW function
    def get_top_n_accounts(self, n):
        """
        Returns a list of account numbers (1-indexed) for the top n accounts with the most transactions.
        In case of ties, lower-numbered accounts are prioritized.
        """
        sorted_accounts = sorted(
            range(1, len(self.accounts) + 1),
            key=lambda acc: (-self.transaction_counts[acc - 1], acc),
        )
        return sorted_accounts[:n]


# Example usage:
if __name__ == "__main__":
    bank = Bank([100, 200, 300])
    bank.deposit(1, 50)  # Account 1 becomes 150; transactions: 1.
    bank.withdraw(2, 100)  # Account 2 becomes 100; transactions: 1.
    bank.transfer(
        3, 1, 150
    )  # Account 3 becomes 150, account 1 becomes 300; transactions: account 3 +1, account 1 +1.

    top_accounts = bank.get_top_n_accounts(2)
    print("Top accounts by transactions:", top_accounts)
