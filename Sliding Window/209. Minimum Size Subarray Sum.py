class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left , right = 0, 0
        temp_sum = 0
        ans = float("inf")
        while right < len(nums):
            temp_sum += nums[right]
           
            while left <= right and temp_sum >= target:
                if ans > right - left + 1:
                    ans = right - left + 1
                temp_sum -= nums[left]
                left += 1

            right += 1
        
        return 0 if ans == float("inf") else ans 