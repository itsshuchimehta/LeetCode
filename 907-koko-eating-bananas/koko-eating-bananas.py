class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for p in piles:
                hours += ceil(p / k)
            
            return hours <= h
        
        L = 1
        R = max(piles)

        while L < R:
            k = (L+R)//2
            if k_works(k):
                R = k
            else:
                L = k + 1
        return L