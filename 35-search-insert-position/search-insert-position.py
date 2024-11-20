class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        L, R = 0, N-1

        while L < R:
            mid = L + ((R-L)//2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                R = mid - 1
            else:
                L = mid + 1
            
        return L + 1 if target > nums[L] else L
        


