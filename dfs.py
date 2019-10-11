# DFS in matrix

    m, n = len(grid), len(grid[0])
    self.res = 0
    def dfs(x, y, val):
        self.res = max(self.res, val)
        for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= i < m and 0 <= j < n and grid[i][j] != 0: #grid[i][j] != 0 is the rule provided by the question
                v = grid[i][j]
                grid[i][j] = 0
                dfs(i, j, val + v)
                grid[i][j] = v
