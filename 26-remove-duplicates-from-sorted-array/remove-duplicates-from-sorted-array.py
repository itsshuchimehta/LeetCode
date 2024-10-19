class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize the first pointer
        i = 0

        # Traverse the list starting from the second element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]  # Place the next unique element

        # The number of unique elements is i + 1
        return i + 1