class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cntOne, cntFlip = 0,0
        for char in s:
            if char == '1':
                cntOne += 1
            else:
                cntFlip += 1
                cntFlip = min(cntFlip, cntOne)
            
        return cntFlip
        
