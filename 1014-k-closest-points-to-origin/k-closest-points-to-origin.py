import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        d = []
        for p in points:
            distance = (p[0]**2) + (p[1]**2)
            d.append((-distance, [p[0], p[1]]))
            
        for i in range(len(d)):
            print(d[i])
            if len(heap) < k:
                heapq.heappush(heap, d[i])
            else:
                heapq.heappushpop(heap, d[i])
            
            
        
        return [h[1] for h in heap]
        