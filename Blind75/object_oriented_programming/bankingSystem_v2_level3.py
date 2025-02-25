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


class Bank:
    def __init__(self, balance):
        self.accounts = balance[:]  # Copy initial balances.
        self.transaction_counts = [0] * len(balance)  # Track transactions.
        # NEW LEVEL 3 For pending transfers:
        self.pending_transfers = {}  # dictionary to temp store pending transfers
        self.transfer_counter = 0  # Unique transfer ID generator.

    def deposit(self, account, amount):
        if account < 1 or account > len(self.accounts):
            return False
        self.accounts[account - 1] += amount
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
        self.transaction_counts[src - 1] += 1
        self.transaction_counts[target - 1] += 1
        return True

    def get_top_n_accounts(self, n):
        sorted_accounts = sorted(
            range(1, len(self.accounts) + 1),
            key=lambda acc: (-self.transaction_counts[acc - 1], acc),
        )
        return sorted_accounts[:n]

    ##### NEW LEVEL 3 function
    def initiate_transfer(self, src, target, timestamp, amount):
        """
        Initiates a pending transfer by writing Key (transfer_id) and Value (source, target, timestamp, amount) to dict:
          - Withdraws (withholds) 'amount' from src if possible.
          - Stores the transfer details with the provided 'timestamp'.
          - Returns a unique string like "TransferX" (where X is an ordinal number).
        Returns "TransferFailed" if the transfer cannot be initiated.
        """

        # Check if both account numbers are within bounds and source account has enough amount
        if (
            src < 1
            or src > len(self.accounts)
            or target < 1
            or target > len(self.accounts)
            or self.accounts[src - 1] < amount
        ):
            return "TransferFailed"

        # Withhold the money from the source.
        self.accounts[src - 1] -= amount
        self.transaction_counts[src - 1] += 1

        # Create a unique transfer id.
        self.transfer_counter += 1
        transfer_id = f"Transfer{self.transfer_counter}"
        # Write transfer specs to pending dict as a dict itself
        self.pending_transfers[transfer_id] = {
            "src": src,
            "target": target,
            "timestamp": timestamp,  # Transfer initiation time.
            "amount": amount,
        }
        return transfer_id

    ##### NEW LEVEL 3 function
    def accept_transfer(self, transfer_id, acceptance_timestamp):
        """
        Accepts a pending transfer if accepted within 24 hours (86400 seconds) of initiation.
          - Deposits the withheld money to the target account.
          - Removes the pending transfer from dict.
        Returns True if the transfer is accepted, else False.
        """
        # Check if given ID exists in pending dict
        if transfer_id not in self.pending_transfers:
            return False

        # Read out transfer_id's value
        pending = self.pending_transfers[transfer_id]

        # Check if acceptance (now) is less than 24h from transfer initiation
        if acceptance_timestamp - pending["timestamp"] > 86400:
            return False

        # Deposit amount in target account
        target = pending["target"]
        self.accounts[target - 1] += pending["amount"]
        self.transaction_counts[target - 1] += 1

        # Remove the pending transfer from dict
        del self.pending_transfers[transfer_id]
        return True


# Example usage:
if __name__ == "__main__":
    bank = Bank([100, 200, 300])

    # Level 1 operations:
    bank.deposit(1, 50)
    bank.withdraw(2, 100)
    bank.transfer(3, 1, 150)

    # Level 2 operation:
    # print("Top accounts:", bank.get_top_n_accounts(2))

    # Level 3 operations:
    # 3.1 Initiate a pending transfer from account 1 to account 2 at timestamp 1000000.
    t_id = bank.initiate_transfer(1, 2, 1000000, 50)
    print("Initiated transfer:", t_id)

    # 3.2 Accept the transfer within 24 hours (e.g., after 1 hour).
    accepted = bank.accept_transfer(t_id, 1000000 + 3600)
    print("Accepted transfer within 24h:", accepted)

    # 3.3 Attempt to accept a transfer after the 24-hour window:
    t_id2 = bank.initiate_transfer(1, 3, 2000000, 30)
    accepted2 = bank.accept_transfer(t_id2, 2000000 + 90000)  # 25 hours later.
    print("Accepted transfer after 24h:", accepted2)
