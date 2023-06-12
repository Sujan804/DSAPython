class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp = {}
        n,m = len(grid), len(grid[0])
        print(n,m)
        def dfs(i,j):
            if i == n-1 and j == m-1:
                return grid[n-1][m-1]
            if (i,j) in dp:
                return dp[(i,j)]
            res1, res2 = float('inf'),float('inf') 

            if i<n-1:
                res1 = dfs(i+1,j) + grid[i][j]
            if j<m-1:
                res2 = dfs(i,j+1) + grid[i][j]
            
            dp[(i,j)] = min(res1, res2)

            return dp[(i,j)]
        
        return dfs(0,0)