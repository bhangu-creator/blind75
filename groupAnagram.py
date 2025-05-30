from collections import Counter
from typing import List


class Solution:
    
    #the following approach used is very similar as used in valid Anagram, in that we used to compare two dictionaries but now we use counter to get frequency of each string in string array and then verify if that frequency exist in the dictionary , we put the frequency as keys and we pair the valid string with same frequency in the values of the dictionary
    #the problem with approach is its time complexity, since we are using counter it returns list but we can not use list to loop through in dictioanry as lists are mutable. so we are converting the output of counter which is list to tuple and we are also sorting the output. The sorting is very necessary as if not done the logic will fail, because lets say counter returns tuple for "eat" as (e=1:a=1:t=1) now for "ate" which is a valid anagram of "ate", counter will return tuple (a=1:t=1:e:1) as you can see both are vaid but the output of counter makes them invalid. so sorting will produce same output as (a=1:e=1:t=1).
    #now becasue of sorting the time complexity is O(m*n)+ mlog(m). O(m*n)mlog(m), mlog(m) is coming from sorting. here n is length of strs and m is length of maximum string in array
    def groupAnagramsLessEfficent(self, strs: List[str]) -> List[List[str]]:
        mydict={}
        retStr=[]
        for s in strs:
            counter = Counter(s)
            if tuple(sorted(counter.items())) in mydict :  
                mydict[tuple(sorted(counter.items()))].append(s)
            else :
                mydict[tuple(sorted(counter.items()))]=[s]

        for key,values in mydict.items():
            retStr.append(values)

        return retStr
    
    
    
    #now we can write an efficent code than written above, The time complexity of the code will be O(m*n). This will get rid of sorting
    #now the approach is very simple. First we will initialize a 26 length of array and all the values will be 0.Then we will loop over strs array and for each word we will count the frequency of each character and then will store it in that 26 length array. you need to imagine the array as every index is a word of english starts from a and end at z. if the word is "ate" than the respective indexes will get updated with their count. And we will store that array/list as tuple in the keys of dictioanry and the value will be the word. so then for each word we will again update that array from scratch and then will use tha converted tuple to look into dict to get a match, if we got the match then we will append that word at that key .
    #Using this approach we have get rid of sorting thus making our code more efficent

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        valDict={}
        alpha_dict={}
        start_ascii=ord('a')
        for i in range(0,26):
            value = i
            key=chr(i+start_ascii)
            alpha_dict[key]=value
        for word in strs:
            freq=[0]*26
            for charc in range(0,len(word)):
                freq[alpha_dict[word[charc]]]=freq[alpha_dict[word[charc]]]+1
            if tuple(freq) in valDict:
                valDict[tuple(freq)].append(word)
            else:
                valDict[tuple(freq)]=[word]  
            freq.clear()
        return list(valDict.values())
        
    
sol=Solution()
strArr=sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(strArr)