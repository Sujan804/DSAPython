import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = collections.Counter(nums).most_common()
        b = []
        for i in range(k):
            b.append(a[i][0])
        return b