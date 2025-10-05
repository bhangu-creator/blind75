
from queue import deque
from typing import List
from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj=defaultdict(set)
        indegree=defaultdict(int)

        for word in words:
            for ch in word:
                if ch not in adj:
                    adj[ch] = set()

        def edgeAndDegree(s1,s2):
            indx=0
            while indx<len(s1) and indx<len(s2):
                if s1[indx]!=s2[indx]:
                    if s2[indx] not in adj[s1[indx]]:
                        adj[s1[indx]].add(s2[indx])
                        indegree[s2[indx]]+=1
                    return True
                indx+=1
            if len(s1)>len(s2):
                return False
            return True

        lcindx=0
        while lcindx<len(words)-1:
            if not edgeAndDegree(words[lcindx],words[lcindx+1]):
                return ""
            lcindx+=1
        queue=deque()
        for ch in adj:
            if indegree[ch]==0:
                queue.append(ch)
        retrStr=""
        while queue:
            node=queue.popleft()
            retrStr+=node
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        if len(retrStr)<len(adj):
            return ""
        return retrStr



#the intuation is to use topological sort . every word in words dict are sorted like the words in dictionary . if anyof the characters in the two
#words are not matching then the word in first string is less than the second string making an edge between two
#we use the indegree method to get the topological sort, we use set to avoid duplicate edges
#also if any string one is greater then string 2 that means that the TC is inavlid and return ""
#the time and space is O(V+E)
        