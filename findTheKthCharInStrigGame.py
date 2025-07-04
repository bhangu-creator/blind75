class Solution:

    #this is called simulation method , this works as the constraints are so small tha we can build a string of 500 char orless and just return the character 
    #it is not optimal for big length string, time and space complexity is O(k) where k is the length of the string
    def kthCharacter(self, k: int) -> str:
        word='a'
        while len(word)<k:
            newstr=""
            for char in word:
                newstr+=chr(ord(char)+1) if char !='z' else 'a'
            word+=newstr
        return word[k-1]
    
    #this is a recursive apprroach and it is very tricky, if we see the pattern of string increase we can say that it is increasing in a way of 1->2->4->8->16->32
    #this way we can say if a string is of length 8 and then if it in next step it becomes of length 16 all the character of that 16 length string will be same as 8 length string but with +1 transformation meaning evry character will be changed to its next character in alphabetic order
    #so if we want to find out kth character we can first find out the highest power of 2 nearest to it lests say k=14 so our power will be 8 now we know k=14 so this means every character of that string is just +1 of string 8 so we can do k-8 that way we will know the place of that charcter in string 8 so it will come as 6 so this means that character at place 6 of 8 length string is what transfomed to 14th place of string lenth 16
    #then using recursion we can again subtract highest power which is 4 means 6-4 so this means character at 2nd place of 4 len string is what is at 6th place of 8 len string the so on 2-1 which gives us 1 which is our base so it returns 0 .. so now we backtrack and find no of transformations a took it will come to 3 so a+3= d that is the answer
    #time and space is Ologk
    def kthCharacter(self, k: int) -> str:
        def dfs(k):
            if k==1:
                return 0
            half=1
            while half*2<k:
                half*=2
            return dfs(k-half)+1
        return chr(ord('a')+dfs(k)%26)

    #this is a bit manipulation solution
    #it is a fact that no of set bits as k-1 gives us transformation no which has a gone through so just added that in "a" to get answer
    #time complexity is Ologk-1 and space is O(1)
    def kthCharacter(self, k: int) -> str:
        return chr(ord('a')+bin(k-1).count('1'))
