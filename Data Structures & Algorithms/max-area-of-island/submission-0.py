class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_count = 0
        count = 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            

            if (min(r, c) < 0 or c == COLS or r == ROWS):
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            
            grid[r][c] = 0

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            
            

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    count = dfs(i, j)
                    if count > max_count:
                        max_count = count
        
        return max_count