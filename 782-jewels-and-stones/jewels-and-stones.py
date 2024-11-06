# from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # stoneCounter = defaultdict(int)
        counter = 0
        for s in stones:
            if s in jewels:
                # stoneCounter[s] += 1
                counter += 1
        return counter