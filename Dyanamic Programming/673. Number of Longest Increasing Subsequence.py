class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lenLIS, res = 0,0
        dp = {}
        for i in range(0, len(nums)):
            maxCnt, maxLen = 1,1
            for j in range(0,i):
                if nums[j]<nums[i]:
                    length, cnt = dp[j]
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length+1, cnt
                    elif length + 1 == maxLen:
                        maxCnt += cnt
            if maxLen>lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt

            dp[i] = [maxLen, maxCnt]
        return res
             
