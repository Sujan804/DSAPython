class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        num_str = ""

        while x:
            digit = x%10
            x = x//10
            num_str += str(digit)

        if num_str == num_str[::-1]:
            return True
        else:
            return False
        