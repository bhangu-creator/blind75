from typing import List
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        def find(u,parent):
            if parent[u]==u:
                return u
            parent[u]=find(parent[u],parent)
            return parent[u]
        def Union(u,v,parent,rank):
            pu=find(u,parent)
            pv=find(v,parent)
            if pu==pv:
                return
            if rank[pu]>rank[pv]:
                parent[pv]=pu
            elif rank[pu]<rank[pv]:
                parent[pu]=pv
            else:
                parent[pv]=pu
                rank[pu]+=1
        parent={chr(alph):chr(alph) for alph in range(97,123)}
        rank={chr(alph):0 for alph in range(97,123)}
 
        for word in equations:
            if word[1]=='=':
                Union(word[0],word[3],parent,rank)
        for word in equations:
            if word[1]=='!':
                if find(word[0],parent)==find(word[3],parent):
                    return False
        return True
        
            