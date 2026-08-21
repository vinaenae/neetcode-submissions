class Solution:
    def isValid(self, s: str) -> bool:
        valid = {']':'[', ')':'(', '}':'{'}
        stack = []
        flag = False
        for i in range(len(s)):
            if s[i] in valid:
                if stack and valid[s[i]] == stack[-1]:
                    stack.pop()
                    flag = True
                else:
                    return False
            else:
                stack.append(s[i])
        return False if stack else True



        