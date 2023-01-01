class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid = int(left +  (right-left)/2)
            if nums[mid]<=nums[mid+1] and nums[mid]<=nums[mid-1]:
                return nums[mid]
            elif nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid-1

        return nums[left]
