class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = []
        for i in range(len(position)):
            lst.append((position[i], speed[i]))
        lst.sort(reverse=True)
         
        stack = []
        for i in range(len(lst)):
            time = (target - lst[i][0]) / lst[i][1]
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


        