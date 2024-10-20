class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverseHelper(l, r, nums):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l = l + 1
                r = r - 1

        # Reverse the whole array
        reverseHelper(0, len(nums)-1, nums)

        # Reverse first k elm
        reverseHelper(0, k - 1, nums)

        #Reverse the other portion
        reverseHelper(k, len(nums)-1, nums)


        
