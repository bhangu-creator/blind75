# solving problem of finding sum of n numbers using recursion approach

class Recur:
    
    def sumOfN(self,n):
        
        #defining the base case to ultimately stop the recursion
        if n==1:
            return 1
        
        #calling the function by dividing the problem into subProblems
        return n+self.sumOfN(n-1)
        
rec= Recur()
val=rec.sumOfN(5)
print( val)
    