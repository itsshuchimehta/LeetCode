class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L = 1
        R = num

        if num == 1:
            return True 

        while L <= R:
            M = (L + R)//2
            if (M ** 2) == num:
                return True
            elif (M ** 2) > num:
                R = M - 1
            else:
                L = M + 1
        
        return False
             