import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # for each coordinate do a func and store the diff in dict: coordinates : diff
        # and add this diif to heap to heapify then 
        # do heap on each oordinete 
        # then heappop until 
        res = []
        heap = []
        dic = {} #coord : diff
        X, Y = 0, 0
        for coordinate in points:
            x, y = coordinate[0], coordinate[1]
            diff = math.sqrt((x - X)**2 + (y - Y)**2)
            dic[tuple(coordinate)] = diff

        for val in dic.values():
            heapq.heappush(heap, val)

        while heap and len(res) < k:
            popped = heapq.heappop(heap)
            for coordinate, diff in dic.items():
                if dic[tuple(coordinate)] == popped:
                    res.append(list(coordinate))

        return res


