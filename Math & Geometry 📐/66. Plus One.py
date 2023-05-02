class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digits = []
        digits.reverse()

        carry = 1
        for digit in digits:
            new_digit = (digit + carry)%10
            carry = (digit + carry)//10
            new_digits.append(new_digit)
        if carry:
            new_digits.append(carry)
        
        new_digits.reverse()

        return new_digits
            
        