class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(r + 1, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for row in matrix:
            row.reverse()
