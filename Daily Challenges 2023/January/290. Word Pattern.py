class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_str = s.split()
        if(len(pattern)!=len(split_str)):
            return False
        mapp = {}
        Set = set()
        for i in range(len(split_str)):
            if split_str[i] in mapp:
                if mapp[split_str[i]] != pattern[i]:
                    return False
            else:
                if pattern[i] in Set:
                    return False 
                mapp[split_str[i]] = pattern[i]
                Set.add(pattern[i])

        print(mapp)
        return True