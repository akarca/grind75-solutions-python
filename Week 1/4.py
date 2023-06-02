"""
Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 104
"""
import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Constraint: prices.length>=1
        # if not prices:
        #     return 0

        buy_price = prices[0]
        max_profit = 0

        for sell_price in prices[1:]:
            new_profit = sell_price - buy_price
            if new_profit > max_profit:
                max_profit = new_profit

            if sell_price < buy_price:
                buy_price = sell_price

        return max_profit


class TestCase(unittest.TestCase):
    def test_maxProfit(self):
        sol = Solution()
        test_cases = [
            ([7, 1, 5, 3, 6, 4], 5),
            ([2, 1, 2, 1, 0, 1, 2], 2),
            # ([], 0),  # Constraint: prices.length>=1
            ([7, 6, 4, 3, 1], 0),
            ([1, 2, 5, 3, 6, 4, 10], 9),
            ([2, 3, 2, 3, 4, 2, 2, 1, 0], 2),
            ([4, 4, 4, 4], 0),
        ]
        for case in test_cases:
            self.assertEqual(sol.maxProfit(case[0]), case[1])


if __name__ == '__main__':
    unittest.main()
