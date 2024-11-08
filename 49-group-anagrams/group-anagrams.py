class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap ={}

        for s in strs:
            sortS = tuple(sorted(s))
            hashmap[sortS] = hashmap.get(sortS, [])
            hashmap[sortS].append(s)
       
        return list(hashmap.values())