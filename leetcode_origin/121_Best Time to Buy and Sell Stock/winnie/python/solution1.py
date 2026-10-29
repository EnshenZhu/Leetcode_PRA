class Solution:
    def maxProfit(self, prices):
        temp_profit = 0
        max_profit = 0

        for money in prices:
            temp_profit = money - temp_profit
            if temp_profit < money:
                temp_profit = money
            max_profit = max(max_profit, temp_profit)


print(Solution.maxProfit(Solution, [7, 1, 5, 3, 6, 4]))