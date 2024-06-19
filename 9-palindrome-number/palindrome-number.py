class Solution:
    def isPalindrome(self, x: int) -> bool:
        revNum = 0
        theNum = x
        sameNum = False
        while x > 0:
            lastdigit = x % 10
            revNum = (revNum * 10) + lastdigit
            x = x // 10
        if revNum == theNum:
            sameNum = True
        return sameNum    
