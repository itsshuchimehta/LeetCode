class Solution:
    def check(self, nums: List[int]) -> bool:
        counter: int = 0
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                counter += 1
        if nums[-1] > nums[0]:
            counter += 1
        return counter <= 1