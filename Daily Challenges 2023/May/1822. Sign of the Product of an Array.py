class Solution:
    def arraySign(self, nums: List[int]) -> int:
        num = 1
        for n in nums:
            num *= n
        
        if num<0:
            return -1
        if num == 0:
            return 0
        return 1