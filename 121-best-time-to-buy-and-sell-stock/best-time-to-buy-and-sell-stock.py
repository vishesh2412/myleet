class Solution(object):
    def maxProfit(self, prices):
        min_cost=float('inf')
        max_profit=0
        for i in prices:
            min_cost=min(i,min_cost)
            max_profit=max(max_profit,i-min_cost)
        return max_profit