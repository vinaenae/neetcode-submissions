class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                l, s  = stack.pop()
                arr[s] = i - s
            stack.append((t, i))
        return arr
                
            
