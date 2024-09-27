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
    """
    # initialize a dp list with a maximum default value (amount + 1) or math.inf,
    #  index is the same as sub-amount, last is amount.
    default_value = amount + 1
    dp = [default_value for i in range(amount + 1)]
    # amount 0 requires zero coins and can be pre-populated
    dp[0] = 0

    # iterate over all sub-amt up to amount (need plus one, since range stops one before)
    for a in range(1, amount + 1):
        # for each sub-amt, check all coins
        for c in coins:
            # you can use that coin only if you don't end in the negative
            if a - c >= 0:
                # THIS IS IT:  update dp at index/amount -> minimum of itself and dp value of amount and current
                # coin subtracted. If the min does not update, the default value remains
                dp[a] = min(dp[a], 1 + dp[a - c])

    # return the last value of dp list, which is the index for the 'amount', if the value is NOT the default value.
    # If the element IS the default value and was not updated (coin combo not possible) then return -1.
    return dp[amount] if dp[amount] != default_value else -1


def main():
    print(coinChange(coins=[1, 2, 5], amount=11), "expected: 3")
    print(coinChange(coins=[2], amount=3), "expected: -1")
    print(coinChange(coins=[1], amount=0), "expected: 0")
    print(coinChange(coins=[1], amount=1), "expected: 1")
    print(coinChange(coins=[1], amount=2), "expected: 2")


if __name__ == "__main__":
    main()
