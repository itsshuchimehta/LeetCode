class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2

            #Middle value is the target
            if target == nums[mid]:
                return mid

            #Left side of the sorted list
            elif nums[lo] <= nums[mid]:
                if target > nums[mid] or target < nums[lo]:
                    lo = mid + 1
                else:
                    hi = mid - 1

            #Right side of the sorted list
            else:
                if target < nums[mid] or target > nums[hi]:
                    hi = mid - 1
                else:
                    lo = mid + 1
                    
        return -1
