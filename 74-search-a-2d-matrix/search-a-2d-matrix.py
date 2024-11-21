class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        L = 0
        R = t - 1

        while L <= R:
            mid = (L + R)//2
            i = mid // n
            j = mid % n
            mid_val = matrix[i][j]

            if mid_val == target:
                return True
            elif target < mid_val:
                R = mid - 1
            else:
                L = mid + 1

        return False