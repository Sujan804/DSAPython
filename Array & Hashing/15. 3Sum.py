class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        res = []
        nums.sort()
        for i in range(0,l-2):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            low = i+1
            high = l-1
            while low<high:
                if (nums[i]+nums[low]+nums[high])==0:
                    res1 = [nums[i],nums[low],nums[high]]
                    res.append(res1)
                    while low<high and nums[low]==nums[low+1]:
                        low += 1
                    while low<high and nums[high]==nums[high-1]:
                        high -= 1
                    low +=1
                    high -= 1
                elif ((nums[i]+nums[low]+nums[high]))<0:
                    low += 1
                else :
                    high -= 1
        return res
                           
            # for j in range (i+1, l-1):
#                 low = j+1
#                 high = l-1
                
#                 while low<=high:
#                     mid = int((low+high)/2)
#                     if nums[i]+nums[j]+ nums[mid] == 0:
#                         res1 = [nums[i],nums[j],nums[mid]]
#                         res1.sort()
#                         if(res1 not in res):
#                             res.append(res1)
#                         break
#                     elif (nums[i]+nums[j]+nums[mid])<0:
#                         low = mid+1
#                     else :
#                         high = mid-1
        # return res
        