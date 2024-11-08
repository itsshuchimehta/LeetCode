class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupnums = set()

        for num in nums:
            if num in dupnums:
                return True
            else:
                dupnums.add(num)
        
        return False