class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimal = float('inf')
        L = 0
        summ = 0
        for R in range(len(nums)):
            summ += nums[R]
                
            while summ >= target:
                minimal = min(minimal,  R - L + 1)
                summ -= nums[L]
                L += 1
        
        return minimal if minimal < float('inf') else 0
