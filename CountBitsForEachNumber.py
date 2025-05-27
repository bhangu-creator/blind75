# In this problem, we have to count the number of set bits (1s) in the binary representation 
# of every number from 0 to n. So we use Dynamic Programming to avoid recomputation.

# Let's take an example: number 4 → binary = 100
# If we do integer division by 2 (i.e., 4 // 2 or 4 >> 1), we get 2 → binary = 10

# Now look at this:
# - The binary of 4 is "100"
# - The binary of 2 is "10"
# If we remove the rightmost bit of 4, the remaining bits are exactly the same as 2.

# That means: the number of set bits in 4 = 
#     → number of set bits in 2 + (1 if the last bit of 4 is 1)

# We can check if the last bit is 1 using (4 & 1):
# - If it's 1 (odd number), we add 1 to the count
# - If it's 0 (even number), we add 0

# So the formula becomes:
#   bits[i] = bits[i >> 1] + (i & 1)

# This works for all i from 1 to n, and since we reuse the result of a smaller subproblem (i >> 1),
# this is a perfect example of dynamic programming.



from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        bits=[0]*(n+1)
        for i in range(1,n+1):
            bits[i]=bits[i>>1]+ (i&1)
        return bits
    
sol=Solution()
val=sol.countBits(5)
print(val)

        
        