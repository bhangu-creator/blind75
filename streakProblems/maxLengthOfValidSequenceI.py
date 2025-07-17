from typing import List

class Solution:


#     With the given requirement in the problem there are only 4 possible kind of subsequence we can get :

# We can either get all even number subsequence
# We can also get all odd number subsequence
# We can also get Alternative number subsequence with subsequence starting from Odd Number
# Or we can get Alternative number subsequence with subsequence starting from Even Number
    def maximumLength(self, nums: List[int]) -> int:
        odd=even=alter=0
        if len(nums)>0:
            if nums[0]%2==0:
                isOdd=False
            else:
                isOdd=True
        for index in range(len(nums)):
            if nums[index]%2==0:
                even+=1
                if not isOdd:
                    alter+=1
                    isOdd=True
            else:
                odd+=1
                if isOdd:
                    alter+=1
                    isOdd=False
        return max(even,odd,alter)


            
            
        