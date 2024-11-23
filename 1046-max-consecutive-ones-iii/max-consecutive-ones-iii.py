class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w = 0
        num_zero = 0
        n = len(nums)
        L = 0
        for R in range(n):
            if nums[R] == 0:
                num_zero += 1
            
            while num_zero > k:
                if nums[L] == 0:
                    num_zero -= 1
                L += 1
            
            w = (R-L) + 1

            max_w = max(max_w, w)
        
        return max_w