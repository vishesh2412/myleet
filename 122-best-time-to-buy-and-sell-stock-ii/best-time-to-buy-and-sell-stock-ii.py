class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        total=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                total+=prices[i]-prices[i-1]
        return total