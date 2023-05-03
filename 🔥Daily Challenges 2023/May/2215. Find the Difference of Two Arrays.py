class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(), set()

        dict1 , dict2 = {}, {}

        for num in nums1:
            set1.add(num)
        for num in nums2:
            set2.add(num)

        list1, list2 = [], []
       
        for num in nums1:
            if (num not in set2) and (num not in dict1):
                list1.append(num)
                dict1[num] = 1
                
        for num in nums2:
            if num not in set1 and (num not in dict2):
                list2.append(num)
                dict2[num] = 1
                
                

        res = []
        res.append(list1)
        res.append(list2)

        return res