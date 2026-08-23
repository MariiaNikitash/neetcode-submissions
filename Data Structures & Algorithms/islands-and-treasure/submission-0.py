class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        

        def addCell(r, c):
            if (min(r, c) < 0 or r == rows or c == cols or
                (r, c) in visited or grid[r][c] == -1
            ):
                return
            visited.add((r, c))
            q.append([r, c])
            



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append([row, col])
                    visited.add((row, col))

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1


            