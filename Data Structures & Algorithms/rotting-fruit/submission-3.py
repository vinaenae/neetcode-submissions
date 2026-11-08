class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        rotten = []
        num_minutes = 0
        fresh = 0

        def bfs(rotten):
            nonlocal num_minutes
            nonlocal fresh
            queue = collections.deque(rotten)
            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            while queue and fresh:
                for _ in range(len(queue)):
                        start, end = queue.popleft()
                        for s, e in directions:
                            r = start + s
                            c = end + e
                            if 0 <= r < ROWS and 0 <= c < COLS:
                                    if grid[r][c] == 1:
                                        grid[r][c] = 2
                                        queue.append((r, c))
                                        fresh -= 1
                num_minutes += 1
            return num_minutes if fresh == 0 else -1

 
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
                
        return bfs(rotten)


