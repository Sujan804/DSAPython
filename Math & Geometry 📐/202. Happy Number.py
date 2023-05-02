class Solution:
    def isHappy(self, n: int) -> bool:
        prev_num = n
        new_num = 0
        nums_map = {}
        while 1:
            temp = prev_num
            if prev_num in nums_map:
                return False
            nums_map[prev_num] = 1
            while temp:
                last_digit = temp%10
                temp = temp//10
                new_num += last_digit*last_digit
            if new_num == 1:
                return True
            prev_num = new_num
            new_num = 0




