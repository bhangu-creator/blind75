from typing import List

class Solution:
    
    #The two main difference between this problem and its's first Part is that we can buy and sell as any times we want in this problem
    # This means that we can also buy the same day we sell, given that we sell the stock at first
    # so the approach is simple we must sell at every dip in the stock to get the max profit, so whenever the price is high than the yesterday we will sell and add the profit 
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit=profit+(prices[i]-prices[i-1])
        return profit
    
sol=Solution()
val=sol.maxProfit([7,1,5,3,6,4])
print(val)




