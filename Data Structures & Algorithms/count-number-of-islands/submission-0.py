class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        valid = set()
        islands = 0

        def bfs(i, j):
            valid.add((i, j))
            queue = collections.deque()
            queue.append((i, j))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while queue:
                first, second = queue.popleft()
                for dr, rc, in directions:
                    r, c = first + dr, second + rc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in valid):
                        queue.append((r, c))
                        valid.add((r, c))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in valid:
                    bfs(i, j)
                    islands += 1
        return islands 