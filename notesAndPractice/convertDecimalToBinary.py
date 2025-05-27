

class Conversion:
    
    #using divided by 2 approach to get the binary equalent of decimal number
    def decToBin(self,n,binArr):
        
        if n==0:
            return
        
        self.decToBin(n//2,binArr)
        
        binArr.append(str(n%2))
    
    #using the bitwise operators & and >> 
    
    def dectoBinBit(self,n):
        bit=""
        while n>0:
            bit=bit+str(n&1)
            n=n>>1
        return bit[::-1]
        


col=Conversion()
binArr=[]
val=col.decToBin(8,binArr)
print("".join(binArr))
s=col.dectoBinBit(25)
print(s)