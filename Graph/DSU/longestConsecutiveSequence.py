from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        uniq_elem=set()
        for num in nums:
            uniq_elem.add(num)
        max_count=1
        for num in uniq_elem:
            if num-1 not in uniq_elem:
                count=1
                current=num
                while current+1 in uniq_elem:
                    current+=1
                    count+=1
                max_count=max(max_count,count)
        return max_count
    #using DSU:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        def find(elem, parent):
            if elem == parent[elem]:
                return elem
            parent[elem] = find(parent[elem], parent)
            return parent[elem]

        def union(elem1, elem2, rank, parent, size):
            par_1 = find(elem1, parent)
            par_2 = find(elem2, parent)
            if par_1 == par_2:
                return size[par_1]  # already in same group

            if rank[par_1] > rank[par_2]:
                parent[par_2] = par_1
                size[par_1] += size[par_2]
                return size[par_1]
            elif rank[par_1] < rank[par_2]:
                parent[par_1] = par_2
                size[par_2] += size[par_1]
                return size[par_2]
            else:
                parent[par_2] = par_1
                rank[par_1] += 1
                size[par_1] += size[par_2]
                return size[par_1]

        uniq_elem = set(nums)
        parent = {}
        rank = {}
        size = {}
        max_size = 0

        for num in uniq_elem:  # use set to avoid duplicates
            parent[num] = num
            rank[num] = 0
            size[num] = 1

        for num in uniq_elem:
            if num + 1 in uniq_elem:
                max_size = max(max_size, union(num, num + 1, rank, parent, size))
            if num - 1 in uniq_elem:
                max_size = max(max_size, union(num, num - 1, rank, parent, size))

        return max_size if max_size > 0 else 1


            
        