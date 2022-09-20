"""
Leetcode 121. Best Time to Buy and Sell Stock (easy)

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


def maxProfitTwoPointer(prices):
    """
    left_pointer = buy, right_pointer = sell
    """
    # initialize both pointers both on the indices at left end of array next to each other
    left_pointer, right_pointer = 0, 1
    max_profit = 0

    # loop until right pointer reaches end of array
    while right_pointer < len(prices):

        # case it is profitable, calc profit and later move pointer
        if prices[left_pointer] < prices[right_pointer]:
            profit = prices[right_pointer] - prices[left_pointer]
            max_profit = max(profit, max_profit)
        # case it is NOT profitable, move pointers
        else:
            left_pointer += 1  # left_pointer = right_pointer

        # regardless of profit or not, move right pointer
        right_pointer += 1
    return max_profit


def main():
    print(maxProfit(prices=[7, 1, 5, 3, 6, 4]), 'expected: 5')
    print(maxProfit(prices=[7, 6, 4, 3, 1]), 'expected: 0')

    print(maxProfitTwoPointer(prices=[7, 1, 5, 3, 6, 4]), 'expected: 5')
    print(maxProfitTwoPointer(prices=[7, 6, 4, 3, 1]), 'expected: 0')


if __name__ == '__main__':
    main()
