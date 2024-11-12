class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        maxA = 0

        while L < R:
            minheight = min(height[L], height[R])
            width = R-L
            area = minheight * width

            maxA = max(maxA, area)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return maxA        

        