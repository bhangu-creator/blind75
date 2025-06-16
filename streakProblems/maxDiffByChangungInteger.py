class Solution:
    
    
    
    #intiuation for this problem is ver simple, to get max diff we need max no and min no possible
    #getting a max no is possible just start from left of nums and swap any first digit that is not 9 to 9 for all the nums
    #to get the min number is a lil bit tricky, in this problme we cannot make no 0 and also cannot have any leading 0. so to get min in this case just swap the first digit to 1 if it is not 1 and if is 1 than start from left and swap any digit which is not 0 to 0 
    
    def maxDiff(self, num: int) -> int:
        s=str(num)
        smin=s
        for ch in s:
            if ch !='9':
                smax=s.replace(ch,'9')
                break
        else:
            smax=s
        if s[0]!='1':
            smin =s.replace(s[0], '1')
        else:
            for ch in s:
                if ch!='0' and ch!=s[0]:
                    smin=s.replace(ch,'0')
                    break
        return int(smax)-int(smin)
    
    
sol=Solution()
val=sol.maxDiff(101)
print(val)
        