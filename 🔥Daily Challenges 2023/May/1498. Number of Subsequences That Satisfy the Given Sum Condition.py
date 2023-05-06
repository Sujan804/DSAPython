class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        answer = 0
        left, right = 0, len(nums)-1
        mod = 10**9 + 7
        nums.sort()
        while left<=right:
            if nums[left] + nums[right] <= target:
                answer = (answer + pow(2, right-left, mod)) % mod
                left += 1
            else:
                right -= 1
        
        return answer
    