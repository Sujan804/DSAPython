class Solution:
    def integerBreak(self, n: int) -> int:

        # if(n == 2 or n == 3):
        #     return n-1
        
        # dp = [-1]*(n+1)
        
        # def helper(num: int):
        #     if num == 0:
        #         return 1
        #     if dp[num] != -1:
        #         return dp[num]
            
        #     res = 1
        #     for i in range (1, num+1):
        #         res = max(res, i*helper(num-i))

        #     dp[num] = res
        #     return dp[num] 
        # return helper(n)

        dp = [0,0,1,2]

        for i in range(4, n+1):
            dp.append(max(max(2*dp[i-2], 2*(i-2)), max(3*dp[i-3], 3*(i-3))))
        return dp[n]
