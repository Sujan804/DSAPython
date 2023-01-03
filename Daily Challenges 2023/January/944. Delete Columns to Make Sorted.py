class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        totalDel = 0
        for i in range(len(strs[0])):
            totalSorted = 1
            for j in range(len(strs)-1):
                if strs[j][i] <= strs[j+1][i]:
                    totalSorted +=1
                else:
                    break
            if totalSorted != len(strs):
                totalDel +=1 
        return totalDel

