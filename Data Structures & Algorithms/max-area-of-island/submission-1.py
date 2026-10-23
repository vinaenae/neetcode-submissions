class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        longest = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        def dfs(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or
                (r, c) in visit or grid[r][c] != 1):
                    return 0
            visit.add((r, c))
            
            return (1 + dfs(r+1, c) +
                dfs(r-1, c) +
                dfs(r, c+1) + 
                dfs(r, c-1))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    longest = max(longest, dfs(r, c))
        return longest