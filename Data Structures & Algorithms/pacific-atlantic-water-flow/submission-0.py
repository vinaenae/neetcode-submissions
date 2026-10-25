class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific = set(), set()

        def dfs(r, c, prevHeight, ocean):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or heights[r][c] < prevHeight or (r, c) in ocean):
                return
            
            ocean.add((r, c))
            prev = heights[r][c]
            dfs(r+1, c, prev, ocean)
            dfs(r-1, c, prev, ocean)
            dfs(r, c+1, prev, ocean)
            dfs(r, c-1, prev, ocean)
        
        for c in range(COLS):
            dfs(0, c, heights[0][c], atlantic)
            dfs(ROWS - 1, c, heights[ROWS-1][c], pacific)
        
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], atlantic)
            dfs(r, COLS-1, heights[r][COLS-1], pacific)
        
        return [list(cell) for cell in (atlantic & pacific)]
        
        