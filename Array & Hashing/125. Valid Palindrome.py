class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for a in s:
            if  (a>= 'a' and a<='z') or (a>='A' and a<='Z') or (a>='0' and a<='9'):
                st += a
        st =  st.lower()
        print(st)
        if st == st[::-1]:
            return True
        else:
            return False