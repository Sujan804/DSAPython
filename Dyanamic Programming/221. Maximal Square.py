class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS  = len(matrix), len(matrix[0])
        
        dp = {}

        def helper(i,j):
            if i >= ROWS or j >= COLS:
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            dp[(i,j)] = 0
            
            if matrix[i][j] == '1':
                right = helper(i,j+1)
                down = helper(i+1, j)
                diag = helper(i+1, j+1)

                dp[(i,j)] = 1 + min(right, down, diag)
            
            return dp[(i,j)]
        
        for i in range(ROWS):
            for j in range(COLS):
                helper(i,j)
        return max(dp.values())**2