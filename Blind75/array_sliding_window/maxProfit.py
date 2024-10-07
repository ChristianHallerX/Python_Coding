"""
121. Best Time to Buy and Sell Stock (easy)

You are given an array 'prices' where 'prices[i]' is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to

sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


def maxProfit(prices):
    max_profit = 0
    lowest_buy = prices[0]

    for price in prices[1:]:
        if price < lowest_buy:
            lowest_buy = price
        else:
            max_profit = max(max_profit, price - lowest_buy)
    return max_profit


def maxProfitTwoPointer(prices: list[int]) -> int:
    """
    Two pointer with array_sliding_window.
    -> Only move pointers if conditions are met and slide only once across the list.
    Left pointer = buy, right pointer = sell
    Time complexity: O(n)
    Space complexity: O(1) no extra objects except profit and pointers, which does not count.
    """

    left = 0  # Buy
    right = 1  # Sell

    maxProfit = 0

    # Move right pointer (sell) forward
    while right < len(prices):
        # Calculate profit when left price is lower than right price
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        else:
            # Move left pointer forward (buy) when left price is higher, so that left (buy) gets lowered
            left = right
        # Always move right (buy) forward
        right += 1

    return maxProfit


def main():
    print(maxProfit(prices=[7, 1, 5, 3, 6, 4]), "expected: 5")
    print(maxProfit(prices=[7, 6, 4, 3, 1]), "expected: 0")

    print(maxProfitTwoPointer(prices=[7, 1, 5, 3, 6, 4]), "expected: 5")
    print(maxProfitTwoPointer(prices=[7, 6, 4, 3, 1]), "expected: 0")


if __name__ == "__main__":
    main()
