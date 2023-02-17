class Solution:
    def cntBit(self, num: int) -> int:
        res = 0
        while num:
            if num & 1:
                res += 1
            num = num>>1
        return res
    def countBits(self, n: int) -> List[int]:
        
        res_arr = []

        for i in range(0,n+1):
            res_arr.append(self.cntBit(i))
        
        return res_arr

       