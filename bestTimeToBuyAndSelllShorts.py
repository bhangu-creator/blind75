
#this problem can be used Two Pointer Approach

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=preProfit=0
        buy=prices[0]
        for price in prices:
            #if the price at ith day is less than the price that I already bought a share before than I will buy the share that day again
            if price<buy:
                buy=price
            else:
             #if the price at ith day is greater than the price I bought my share than I can sell that share at this day but before that I need to verify if the profit from selling that share is gonna bebigger than the profit I already got by selling the previous share  
                preProfit=price-buy
                if profit<preProfit:
                    profit=preProfit
        return profit
    
sol= Solution()
val=sol.maxProfit([7,3,5,6,1,2])
print(val)
            