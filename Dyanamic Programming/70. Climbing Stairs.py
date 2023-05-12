class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        # # way1
        # dp = [0]*n
        # dp[0] = 1
        # dp[1] = 2

        # for i in range(2,n):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n-1]

        # way2

        dp0 = 1
        dp1 = 2
        curr = 0
        for i in range(2,n):
            curr = dp0 + dp1
            dp0 = dp1
            dp1 = curr
        
        return dp1
            