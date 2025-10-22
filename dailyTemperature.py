from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[0]* n
        stack=[]
        for day in range(n):
            curr_temp=temperatures[day]                
            while stack and stack[-1][0]<curr_temp:
                    _,prev_day=stack.pop()
                    day_diff=day-prev_day
                    result[prev_day]=day_diff
            stack.append((curr_temp,day))
        return result
                
    #it uses stack and the time and space is O(n)