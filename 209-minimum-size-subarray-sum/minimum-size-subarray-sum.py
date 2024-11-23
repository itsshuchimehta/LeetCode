class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimal = len(nums) + 1
        L = 0
        summ = 0
        for R in range(len(nums)):
            summ += nums[R]
                
            while summ >= target:
                if summ >= target:
                    w = R - L + 1
                    minimal = min(minimal, w)
                summ -= nums[L]
                L += 1
        
        return minimal if minimal < len(nums) + 1 else 0
