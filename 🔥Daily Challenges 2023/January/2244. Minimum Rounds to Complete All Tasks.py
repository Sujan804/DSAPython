class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        countFreq = Counter(tasks)
        res = 0
        for element in countFreq:
            if countFreq[element] == 1:
                return -1
            res += int((countFreq[element]+2)/3)
        return res
            
        