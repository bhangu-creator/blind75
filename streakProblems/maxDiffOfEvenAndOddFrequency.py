from typing import List


class Solution:
    
    #so here we had to get the max difference between the odd frequency of characters and even frequency of characters
    #we can get the max differecne if one of those thing is max and other is min
    #so first we get the frequencies for every character and stored it in a dict
    #then we get the max even freq and min even freq and same for max odd freq and min odd freq
    #then we got the max diff between the (max odd - min even) and (min odd-max even) ,we had to consider both the cases since the difference can also be negative
    
    def maxDifference(self, s: str) -> int:
        dictfreq={}
        maxevenfreq=maxoddfreq=float('-inf')
        minevenfreq=minoddfreq=float('inf')
        for char in s:
            if char not in dictfreq:
                dictfreq[char]=1
            else:
                dictfreq[char]+=1
        for key in dictfreq:
            if dictfreq[key]%2==0:
                maxevenfreq=max(maxevenfreq,dictfreq[key])
                minevenfreq=min(minevenfreq,dictfreq[key])

            else:
                maxoddfreq=max(dictfreq[key],maxoddfreq)
                minoddfreq=min(dictfreq[key],minoddfreq)
        return max((minoddfreq-maxevenfreq),(maxoddfreq-minevenfreq))





    
sol=Solution()
val=sol.maxDifference("mmsmsym")
print(val)
