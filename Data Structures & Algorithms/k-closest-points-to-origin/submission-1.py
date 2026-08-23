import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        
        for coordinate in points:
            x, y = coordinate
            diff = (x**2) + (y**2)
            heap.append((diff, coordinate))

        heapq.heapify(heap)

        while k > 0:
            diff, coord = heapq.heappop(heap)
            res.append(coord)
            k -=1
        return res


