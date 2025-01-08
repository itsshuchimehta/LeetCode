class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        curr_count = [0]
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            else:
                grid[i][j] = 0
                curr_count[0] += 1
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i - 1, j)
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                curr_count[0] = 0
                if grid[i][j] == 1:
                    dfs(i, j)
                    max_area = max(max_area, curr_count[0])
        
        return max_area
