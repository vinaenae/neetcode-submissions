from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        output = [0] * len(temperatures)
        stack = [[temperatures[0], 0]]
        for r in range(1, len(temperatures)):
            if temperatures[r] <= stack[-1][0]:
                stack.append([temperatures[r], r])
            else:
                while stack and temperatures[r] > stack[-1][0]:
                    output[stack[-1][1]] = r - stack[-1][1]
                    stack.pop()
                stack.append([temperatures[r], r])
        return output
                    








        while r < len(temperatures):
            if output[l] != 0:
                l += 1
            else:
                if temperatures[r] > temperatures[l]:
                    output[l] = (r - l)
                    l += 1
                else:
                    if temperatures[r] > temperatures[r-1]:
                        output[r-1] = 1
                    r += 1
        return output
                    
            
