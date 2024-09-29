"""
322. Coin Change (medium)

You are given an integer array 'coins' representing coins of different denominations and an integer 'amount'

representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.

If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""


def coinChange(coins: list[int], amount: int) -> int:
    """
    Dynamic programing solution. Greedy with preference to large coins does NOT work.
    Time Complexity: O(amount * len(coins))
    Memory Complexity: O(amount) for dp_cache
    """
    # Initialize a dp_cache as list e.g., [66666] with a maximum default value (amount + 1) or infinite (math.inf)
    dp_cache = [amount + 1] * (amount + 1)

    # Amount 0 requires zero coins and can be pre-populated
    dp_cache[0] = 0

    # Bottom up from 1 to amount (need plus one, since range stops one before)
    for curr_amnt in range(1, amount + 1):
        # For each curr_amnt, check all coins that don't go negative
        for c in coins:
            if curr_amnt - c >= 0:
                # Recurrence relation: update dp at index/amount -> minimum of itself and dp value of amount
                # and current coin subtracted.
                dp_cache[curr_amnt] = min(
                    dp_cache[curr_amnt], 1 + dp_cache[curr_amnt - c]
                )

    # Return the last value of dp_cache list, which is at the index for the 'amount'.
    # However, if the last value was untouched (it remained amount+1) because did not compute, then return "-1"
    return dp_cache[amount] if dp_cache[amount] != (amount + 1) else -1


def main():
    print(coinChange(coins=[1, 2, 5], amount=11), "expected: 3, explanation: 5+5+1")
    print(coinChange(coins=[2], amount=3), "expected: -1, explanation: impossible")
    print(coinChange(coins=[1], amount=0), "expected: 0")
    print(coinChange(coins=[1], amount=1), "expected: 1")
    print(coinChange(coins=[1], amount=2), "expected: 2")


if __name__ == "__main__":
    main()
