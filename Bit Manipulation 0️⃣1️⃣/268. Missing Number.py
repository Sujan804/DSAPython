class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0 
        for num in nums:
            res = res^num
        for i in range(len(nums)+1):
            res ^= i
        return res