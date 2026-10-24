class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        fresh_oranges = 0

        queue = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh_oranges += 1

        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        num_time = 0
        while queue and fresh_oranges:
            for _ in range(len(queue)):
                rc, cl = queue.popleft()
                for r, c in directions:
                    row, col = r + rc, c + cl

                    if (row < 0 or row == ROWS or col < 0 or col == COLS or
                        grid[row][col] == 0):
                        continue

                    if grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh_oranges -= 1
                        queue.append((row, col))
            num_time += 1


        if fresh_oranges > 0:
            return -1
        return num_time
