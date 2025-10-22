from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res=[]

        def backtrack(path,lcount,rcount):
            if lcount>n or rcount>n or rcount>lcount:
                return 
            if len(path)==2*n:
                res.append(path)
                return
            backtrack(path+")",lcount,rcount+1)
            backtrack(path+"(",lcount+1,rcount)
        backtrack("(",1,0)
        return res
    #ok so it is purely backtracking problem, to undertstand the problem please draw a recursion tree starting from (.
    #time complexity is (2^2*n)n,it is called something conclave numbers we can write it as Cn*n,space is 
        
            



        