class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lenOfNums = len(nums)
        expected_total =  lenOfNums * (lenOfNums + 1)//2
        elm = expected_total - sum(nums)
        return elm 