class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(opened, close, curr):
            if opened == n and close == n:
                res.append(curr)
                return

            if opened < n:
                curr += "("
                dfs(opened + 1, close, curr)
                curr = curr[:-1]
            
            if close < opened:
                curr += ")"
                dfs(opened, close + 1, curr)
                curr = curr[:-1]
        dfs(0, 0, "")
        return res
            
            
        

        