class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1Idx = {}
        for i, n in enumerate(nums1):
            num1Idx[n] = i

        ans = [-1] * len(nums1)

        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = num1Idx[val]
                ans[idx] = curr
            if curr in num1Idx:
                stack.append(curr)
        return ans    
