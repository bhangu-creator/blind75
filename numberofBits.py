



class Solution:
    
#this problem can be solved very easily using bitwise operators like & and >>
#what we are doing is basically checking the LSB(least significant bit) of a number n and if it is 1 then increasing the count
#then after that we are using >> to shift the bits right side which get rid of LSB giving us a new bit to verify
    
    def hammingWeight(self, n: int) -> int:
        count=0
        while n>0:
            if n&1==1:
                count=count+1
            n=n>>1
        return count
    
    #brian Kernighan’s Algorithm:
    #First Observation is this if n is the number then in the binary form of n-1 all the bits will be opposite to n after the Right Set Bit
    #for example if n=10 binary= 1010 and n-1=9 binary 1001 then as noticed all bits after RSB are opposite in n-1 so we did this
    # n&(n-1) all the bits after RSB will become 0 
    #this algo is bettter as it only run as many times as there are set bits in a binary number and it will keep on making bits 0 after RSB ending the program when binary is 000
    
    def KernighanAlgo(self, n: int) -> int:
        count=0
        while n>0:
            n= n&(n-1)
            count=count+1
        return count
    
sol =Solution()
val2=sol.KernighanAlgo(25)
print(val2)

val=sol.hammingWeight(25)
print(val)
