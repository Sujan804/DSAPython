class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        left = 0
        right = length - 1
        maxArea = 0
        while(left<right):
           leftHeight, rightHeight = height[left], height[right]
           
           if leftHeight < rightHeight :
                maxArea = max((leftHeight*(right-left)),maxArea)
                while height[left] <= leftHeight and left<length:
                   left += 1
           else:
                maxArea = max(rightHeight*(right-left), maxArea)
                while height[right] <= rightHeight and right:
                    right -= 1
        
        return maxArea