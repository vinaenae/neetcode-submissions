class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        COLS, ROWS = len(grid[0]), len(grid)
        num_islands = 0
        seen = set()

        def dfs(i, j):
            seen.add((i, j))
            queue = collections.deque([(i, j)])
            directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

            while queue:
                for _ in range(len(queue)):
                    s, e = queue.popleft()
                    for start, end in directions:
                        n_row = s + start
                        n_col = e + end
                        if 0 <= n_row < ROWS and 0 <= n_col < COLS: 
                            if grid[n_row][n_col] == "1" and (n_row, n_col) not in seen:
                                queue.append((s+start, e+end))
                                seen.add((s+start, e+end))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in seen:
                    dfs(i, j)
                    num_islands += 1

        return num_islands