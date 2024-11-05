class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0

        while i < len(nums):
            start = nums[i]
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i+=1
            
            if start != nums[i]:
                result.append(f"{start}->{nums[i]}")
            else:
                result.append(f"{nums[i]}")
            i += 1

        return result



