
import math

class Conversion:
    
    def binaryToDecimal(self,num):
        power=dec=0
        while num>0:
            #extracting the last digit of binary number and if will only works if it is 1
            if num%10==1:
                #1<<power is a clever way of doing 2 rasie to the power, it's basically like shifting 1 on a binary number left 
                dec=dec+(1<<power)
            #removing the last digit from number    
            num=math.floor(num/10)
            power=power+1
        return dec
            
        
        
sol=Conversion()
num=1001
val=sol.binaryToDecimal(num)
print(val)
