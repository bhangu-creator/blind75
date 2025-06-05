class Solution:
    
    #first apporach is very simple just loop from 1 to n and if no is divisible by m than add is num1 either add it in num2
    def differenceOfSums(self, n: int, m: int) -> int:
        num1=num2=0
        for x in range(1,n+1):
            if x%m!=0:
                num1=num1+x
            else:
                num2=num2+x
        return num1-num2
    
    #second approach is using math
    
    def differenceOfSumsUsingMath(self, n: int, m: int) -> int:
        #first calculate the total of n numbers using the following formula
        total=n*(n+1)//2
        #then calculate how many multiples are there of m in n
        k=n//m
        #this is the most important let's say k=3 which would mean that there are 3 multiples of m in 3 and let's just say m=2 and n=7 so k=7//2 meaning k=3 and having 3 multiples of 2 in range 1-7 would look like this:
        # 2*1=2
        #2*2=4
        #2*3=6
        #so there is a pattern if we do this 2*1+2*2+2*3 this is basically is = 2*(1+2+3) so here 2 is m that we know and (1+2+3) is 1 to k we also can calculate that using k*k+1//2 meaning that will give us the following formula:
        divisible=m*(k*(k+1)//2)
        #this is just simple , we needed sum of numbers not divivsible by m - sum of numbers divisible by m, so basically saying (total-divisible) - divisible which became total-2*divisible
        return total-(2*divisible)
    
sol=Solution()
val=sol.differenceOfSumsUsingMath(5,6)
print(val)
        
        

        