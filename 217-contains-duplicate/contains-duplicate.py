class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupnums = {}

        for num in nums:
            if num in dupnums:
                return True
            else:
                dupnums[num] = 1
        
        return False