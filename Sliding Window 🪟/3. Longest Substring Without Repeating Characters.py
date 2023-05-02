class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        startIndex = 0
        
        mapped = {}

        for i in range(len(s)):
            if s[i] in mapped and mapped[s[i]] >= startIndex:
                if maxLength < i - startIndex:
                    maxLength = i - startIndex
                startIndex = mapped[s[i]] + 1
            
            mapped[s[i]] = i
        
        if maxLength < len(s) - startIndex:
            maxLength = len(s) - startIndex
        
        return maxLength