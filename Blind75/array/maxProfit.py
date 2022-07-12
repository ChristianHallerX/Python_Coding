""" Leetcode 121. Best Time to Buy and Sell Stock
You are given an array 'prices' where 'prices[i]' is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to

sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

def maxProfit(prices):
    profit = 0
    lowest_buy = prices[0]

    for price in prices[1:]:
        if price < lowest_buy:
            lowest_buy = price
        else:
            profit = max(profit, price - lowest_buy)
    return profit

def main():
    print(maxProfit(prices=[7,1,5,3,6,4]))
    print(maxProfit(prices=[7,6,4,3,1]))

if __name__ == '__main__':
    main()
