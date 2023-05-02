class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zeroRow = set()
        zeroCol = set()

        for i in range (len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroRow.add(i)
                    zeroCol.add(j)
        
        for r in zeroRow:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
        for c in zeroCol:
            for i in range(len(matrix)):
                matrix[i][c] = 0
        
    

