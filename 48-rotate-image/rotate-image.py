class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the top left
                topLeft = matrix[top][l + i]

                # move the bottom left to the top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move the bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move the top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # add the top left in top right
                matrix[top + i][r] = topLeft

            l += 1
            r -= 1
            