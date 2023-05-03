class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        mx = 0
        l  = len(s)
        mp = {'I': 1, 'V':5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M':1000}
        for i in range(l-1,-1,-1):
            if mp[s[i]] >= mx:
                res += mp[s[i]]
                mx = mp[s[i]]
            else:
                res -= mp[s[i]]
        return res