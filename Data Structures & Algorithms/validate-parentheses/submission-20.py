class Solution:
    def isValid(self, s: str) -> bool:
        stack, count = [], 0
        valid = {'(': ')', '{': '}', '[': ']'}
        # if len(s) % 2 != 0:
        #     return False
        # open = len(s) // 2
        # for char in s:
        #     if char not in valid and count < open:
        #         return False
        #     elif count >= open:
        #         if char != valid[stack.pop()]:
        #             return False
        #     else:
        #         stack.append(char)
        #         count += 1
        # return True
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char in valid:
                stack.append(char)
            elif stack and char != valid[stack[-1]]:
                return False
            elif stack and char == valid[stack[-1]]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        return False
        
            
            




        