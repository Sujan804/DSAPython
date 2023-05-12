class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp0 = cost[0]
        dp1 = cost[1]
        curr = 0

        for i in range(2, len(cost)):
            curr = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = curr

        return min(dp0, dp1)