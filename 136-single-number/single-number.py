class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashArr = {}

        for num in nums:
            if num not in hashArr:
                hashArr[num] = 1
            else:
                hashArr[num] = hashArr[num] + 1
            
        
        Anskey = [k for k, v in hashArr.items() if v == 1]   

        return Anskey[0]

