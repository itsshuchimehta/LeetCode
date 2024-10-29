class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        closest_num = nums[0]
       
        for num in nums:
            if abs(num) < abs(closest_num):
                closest_num = num 
        
        if closest_num < 0 and abs(closest_num) in nums:
            return abs(closest_num)
        
        return closest_num
