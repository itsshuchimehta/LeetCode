class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        L = 0
        R = n - 1

        while L < R:
            mid = L + ((R - L)//2)
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid 
        
        min_index = L

        if min_index == 0:
            L, R = 0, n - 1 
        elif target >= nums[0] and target <= nums[min_index - 1]:
                L, R = 0, min_index - 1
        else:
            L, R = min_index, n - 1

        while L <= R:
            mid = L + ((R - L)//2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                L = mid + 1
            else:
                R = mid - 1
        
        return -1
            
        # while L <= R:
        #     mid = L + ((R-L) // 2)
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > nums[R]: 
        #         if nums[R] > target:
        #             L = mid
        #         else:
        #             L = mid + 1
        #     else:
        #         R = mid - 1     
        
        # return -1