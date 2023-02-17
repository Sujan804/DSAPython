class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt_set_bit = 0
        while n!=0:
            if n&1:
                cnt_set_bit += 1
            n = n>>1
        return cnt_set_bit