

class Solution:
    def minMaxDifference(self, num: int) -> int:  #pacific ocean
        for row in range(4):
            for col in range(4):
                print((row,col), end=' ')
                if row!=0:
                    break
            print()


        
        # for row in range(4):   #atlantic ocean
        #     for col in range(4):
        #         if row!=3 and col!=3:
        #             continue
        #         print((row,col), end=' ')

        # print() 
        

sol=Solution()
val=sol.minMaxDifference(9566477)
print(val)
        
        