class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        sum  = 0
        for i in range(0,l):
            sum += mat[i][i]

        r = 0
        for c in range(l-1,-1,-1):
            sum += mat[r][c]
            r += 1
        
        if l & 1:
            sum -= mat[l//2][l//2]
        
        return sum

