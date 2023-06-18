class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = {}

        def dfs(i,j):
            if len(t) == j:
                return 1
            if i>=len(s) or j > len(t):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            res = 0
            if s[i] == t[j]:
                dp[(i,j)] = dfs(i+1,j) + dfs(i+1, j+1)
            else:
                dp[(i,j)] = dfs(i+1,j)
            return dp[(i,j)]
        return dfs(0,0)

