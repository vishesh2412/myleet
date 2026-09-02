class Solution(object):
    def maxProfit(self, prices):
        min_cost=prices[0]
        max_profit=0
        for i in prices[1:]:
            min_cost=min(i,min_cost)
            max_profit=max(max_profit,i-min_cost)
        return max_profit