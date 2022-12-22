class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 1
        h = len(s)+1
        while l+1<h:
            mid = l+(h-l)//2

            if self._isValidString(s,mid,k):
                l = mid
            else:
                h = mid
        
        return l

    def _isValidString(self, s:str, mid:int,k:int) -> bool:
        
        freqMap = {}
        maxFreq = 0

        start = 0
        for end in range(len(s)):
            freqMap[s[end]] = freqMap.get(s[end],0) +1

            if end+1 -start>mid:
                freqMap[s[start]] -= 1
                start += 1
            maxFreq = max(maxFreq, freqMap[s[end]])

            if mid - maxFreq <= k:
                return True
        return False



