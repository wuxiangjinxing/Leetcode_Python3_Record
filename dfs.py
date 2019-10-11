# DFS find the path with max value in a matrix

def getmaxingrid(self, grid):
    res = 0
    seen = set()
    def DFS(grid, i, j):
        v, path = 0, set() ## v:从该节点往后最长路径的值(不包含该节点), path:从该节点往后最长路径(不包含该节点)
        tmp = grid[i][j]
        grid[i][j] = 0 #This shall be modified based on question
        for m,n in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] != 0: # grid[m][n] != 0 is provided by question
                s, t = DFS(grid, m, n)
                if s > v:
                    v = s
                    path = t
        grid[i][j] = tmp
        return v + tmp, path | {(i, j)}
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) not in seen and grid[i][j] != 0:
                val, path = DFS(grid, i, j)
                if val > res:
                    res = val
                    seen = path
    return res
