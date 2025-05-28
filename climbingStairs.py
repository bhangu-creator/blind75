class Solution:
    def climbStairs(self, n: int) -> int:
       step=()
       if n==1:
        return (1)
       if n==0:
        return (2)
       step = step, (self.climbStairs(n-1),self.climbStairs(n-2))
       return len(step)



       
        
sol=Solution()
val=sol.climbStairs(3)
print(val)