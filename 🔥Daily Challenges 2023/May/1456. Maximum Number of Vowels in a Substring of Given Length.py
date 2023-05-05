class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        def isVowel(c:chr)->bool:
            if c == 'a' or c == 'e' or c=='i' or c =='o' or c=='u':
                return True
            else:
                return False

        l = len(s)
        max_vowel = 0
        cnt_vowel = 0
        for i in range(0,k):
            if isVowel(s[i]):
                cnt_vowel +=1 
        
        max_vowel = cnt_vowel

        for i in range(k, l):
            if isVowel(s[i]):
                cnt_vowel += 1
            if isVowel(s[i-k]):
                cnt_vowel -= 1
            if cnt_vowel>max_vowel:
                max_vowel = cnt_vowel

        return max_vowel