class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        longest_num = 0
        valid = set()


        def bfs(r, c):
            valid.add((r, c))
            curr_num = 1
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            queue = collections.deque()
            queue.append((r, c))
            nonlocal longest_num
            while queue:
                first, second = queue.popleft()

                for rc, cl in directions:
                        row, col = first + rc, second + cl 
                        if row in range(rows) and col in range(cols):
                            if grid[row][col] == 1 and (row, col) not in valid:
                                valid.add((row, col))
                                queue.append((row, col))
                                curr_num += 1
            longest_num = max(longest_num, curr_num)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in valid:
                    bfs(r, c)
        return longest_num
        