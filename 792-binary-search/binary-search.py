class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            # mid = (L+R)//2
            mid = L + (R - L)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                L = mid + 1
            else:
                R = mid - 1
        return -1