class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        L = 0
        R = n - 1

        # Check if the array is rotated, if it is get the index of min of the array
        while L < R:
            mid = L + ((R - L)//2)
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid 
        
        min_index = L

        # Set the index range where the target could be
        if min_index == 0:
            L, R = 0, n - 1 
        elif target >= nums[0] and target <= nums[min_index - 1]:
                L, R = 0, min_index - 1
        else:
            L, R = min_index, n - 1

        # Search for target within that range
        while L <= R:
            mid = L + ((R - L)//2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                L = mid + 1
            else:
                R = mid - 1
        
        return -1

        # TC: O(2 log(n)) == O(lon(n))
        # SC: O(1)