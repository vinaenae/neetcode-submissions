class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(start, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return
            

            i = start
            while i < len(candidates):
                curr.append(candidates[i])
                backtrack(i+1, curr, total + candidates[i])
                curr.pop()
                while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                    i+=1
                i += 1
        backtrack(0, [], 0)
        return res    


