from typing import List

class Solution:

    #this is the dsu(union find) approach ,its not optimal but it is what I came up with so..
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        parent={ path:path for path in folder}
        def union(path1,path2):
            parent[path2]=path1
        def find(path):
            for i in range(2,len(path)):
                char=path[i]
                if char=='/':
                    subFolder=path[:i]
                    if subFolder in parent:
                        union(subFolder,path)
        retArr=[]
        for path in folder:
            find(path)
            if path==parent[path]:
                retArr.append(path)
        return retArr
sol=Solution()
retarr=sol.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])
print(retarr)
        