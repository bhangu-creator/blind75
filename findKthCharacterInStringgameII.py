from typing import List

class Solution:


    #Intuition
# The length of the string doubles at every operation, forming powers of 2:1 → 2 → 4 → 8 → 16 → 32 → ... for each new version of the string:

# If the operation is 0, the right half is an exact copy of the left half.

# If the operation is 1, the right half is a transformed copy, where each character becomes its next character (e.g. 'a' → 'b', 'z' → 'a').

# To find the k-th character, we recursively track where it came from:

# If it came from a copy, the character stays the same.

# If it came from a transformed copy, it was transformed once.

# So, we keep reducing k by subtracting the largest power of 2 (half) smaller than k, and move back in the operation list to check how many times it was transformed.

# The number of transformations (i.e., how many 1s it passed through) tells us how many times to advance 'a':

# chr(ord('a') + num_transformations % 26)

#Approach

# Find the nearest power of 2 ≤ k
# This gives you the length of the previous version of the string (half).

# For example, if k = 13, the previous version must have been of length 8.

# Track the depth

# Every time the string doubles in size, we increase a depth counter.
# This depth tells us how many operations were applied to reach the current string length.

# Move k into the left part of the string
# Since the right half is formed from the left half, we calculate k - half to find where this character came from in the previous string version.

# Determine the correct operation
# The operation that generated the current segment is at index depth in the operations list.

# So, we use operations[depth] to check:

# 0 → character is copied from left (no transformation)

# 1 → character is transformed (add +1 to transformation count)

# Recursively continue

# Each time we go one level deeper, we reduce k, and use the next relevant operation.

# When we reach the base case (k == 1), we know the character was originally 'a'.

# Final result

# Add the total number of transformations to 'a' using:
# chr(ord('a') + transformations % 26)

#timeand space is O(logk)


    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def dfs(k,operation_index):
            if k==1:
                return 0
            half=1
            depth=0
            while half*2<k:
                half*=2
                depth+=1
            newIndex=max(0,operation_index-depth)
            if operations[depth]==0:
                return dfs(k-half,newIndex)
            else:
                return dfs(k-half,newIndex)+1
        return chr(ord('a')+dfs(k,len(operations)-1)%26)