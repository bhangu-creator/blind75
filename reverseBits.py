class Solution:
    #remember this for ever : & is used to get the last bit of a binary number
    #>> is a right shift operator which shifts all the values to the right
    #<< is lefft shift operator which shifts all the values to the left
    # | is an OR operator which if used with any bit (0,1) returns the original bit with no change
    #also remeber a binary number can be stored in simple int variable
    def reverseBits(self, n: int) -> int:
        rev=0
        for _ in range(32):
            rev=(rev<<1) | n&1
            n=n>>1
        return rev
        
sol=Solution()
val=sol.reverseBits(25)
print(val)

            