class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix[0])
        cmatrix = [[0]*l for i in range(l)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                cmatrix[r][c] = matrix[c][r]
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c] = cmatrix[r][c]
        
        for r in range(len(matrix[0])):
            for c in range(len(matrix[0])//2):
                temp = matrix[r][c]
                matrix[r][c] = matrix[r][l-c-1]
                matrix[r][l-c-1] = temp
        