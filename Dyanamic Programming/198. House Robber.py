class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        dp = [-1]*l
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        def max_rob(i:int)->int:
            if (i<0):
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i] = max(nums[i]+max_rob(i-2), max_rob(i-1))
            return dp[i]
            
        return max_rob(l-1)