class Solution:
    def isPalindrome(self, x: int) -> bool:
        revNum = 0
        theNum = x
    
        while x > 0:
            lastdigit = x % 10
            revNum = (revNum * 10) + lastdigit
            x = x // 10
      
        return revNum == theNum    
