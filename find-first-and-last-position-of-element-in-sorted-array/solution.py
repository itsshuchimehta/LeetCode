class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        first = self.first_position(nums, target)

        #If target is not found in the array, return [-1, -1].
        if first == -1:
            return [-1, -1]
        
        result.append(first)
        last = self.last_position(nums, target)
        result.append(last)
        return result
   
    #find the starting position of a given target value.
    def first_position(self,nums,target):
        def condition(mid):
            if nums[mid] == target:
                if mid > 0 and nums[mid - 1] == target:
                    return 'left'
                else:
                    return 'found'
            elif nums[mid] > target:
                return 'left'
            else:
                return 'right'        
        return helper_search(0, len(nums)-1, condition)

    #find the ending position of a given target value.
    def last_position(self,nums,target):
        def condition(mid):
            if nums[mid] == target:
                if mid < len(nums)-1 and nums[mid + 1] == target:
                    return 'right'
                else:
                    return 'found'
            elif nums[mid] > target:
                return 'left'
            else:
                return 'right'        
        return helper_search(0, len(nums)-1, condition)    

#helper function 
def helper_search(lo,hi,condition):
    while lo<= hi:
        mid = (lo + hi) //2
        result = condition(mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1
