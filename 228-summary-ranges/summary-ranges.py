class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i, j = 0,0

        while i <= j and j < len(nums):
            if j < len(nums) - 1 and nums[j] == nums[j + 1] - 1:
                j+=1
            else:
                if i == j:
                    result.append(f"{nums[i]}")
                else:    
                    result.append(f"{nums[i]}->{nums[j]}")
                i = j + 1
                j+=1
        return result




