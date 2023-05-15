class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0
        length = len(nums)
        if(length == 1):
            return nums[0]
        
        temp = 0
        for i in range(length-1):
           temp = max(rob1+nums[i], rob2)
           rob1 = rob2
           rob2 = temp
        
        l_to_r = temp
        
        rob1, rob2 = 0, 0
        for i in range(length-1, 0, -1):
            temp = max(rob1+nums[i], rob2)
            rob1 = rob2
            rob2 = temp
        
        r_to_l = temp
        return max(l_to_r, r_to_l)
        