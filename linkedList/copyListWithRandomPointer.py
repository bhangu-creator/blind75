
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
from typing import Optional

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        headDict={}
        tail=head
        while tail:
            headDict[tail]=Node(tail.val)
            tail=tail.next
        tail=head
        while tail:
            node=headDict[tail]
            node.next=headDict.get(tail.next)
            node.random=headDict.get(tail.random)
            tail=tail.next
        return headDict[head]
    
#time and space is O(n) 
#first pass is used simply to create all the new nodes
#second pass is used to assign the created nodes with there respective random and next pointer
        

