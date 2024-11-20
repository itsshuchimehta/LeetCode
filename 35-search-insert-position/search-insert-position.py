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
            
        if L - R == 0 and target > nums[L]:
            return L + 1
        else:
            return L



