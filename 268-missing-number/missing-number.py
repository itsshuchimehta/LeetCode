class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if i not in nums:
        #         return i
        # return len(nums)
        lenOfNums = len(nums)
        expected_total =  lenOfNums * (lenOfNums + 1)//2
        elm = expected_total - sum(nums)
        return elm 