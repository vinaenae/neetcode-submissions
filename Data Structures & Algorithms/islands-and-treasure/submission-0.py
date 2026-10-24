class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        curr_num = 0
        visit = set()

        queue = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if (row < 0 or row == ROWS or col < 0 or col == COLS or
                    grid[row][col] == -1 or (row, col) in visit):
                    continue

                visit.add((row, col))    
                grid[row][col] = curr_num
                
                queue.append((row+1, col))
                queue.append((row-1, col))
                queue.append((row, col + 1))
                queue.append((row, col - 1))

            curr_num += 1

        
        
        