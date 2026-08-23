class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dimesions 
        rows, cols = len(grid), len(grid[0])
        MaxArea = 0
        visited = set()

        def bfs(r, c):
            directions = [[1,0], [0,1], [-1, 0], [0, -1]]
            q = deque([(r,c)])
            visited.add((r,c))
            area = 1
            while q:
                row, col = q.popleft()
                # check if in bounds
                for dr, dc in directions:
                    new_row, new_col = row+dr, col+dc
                    if (new_row in range(rows) and new_col in range(cols)
                        and grid[new_row][new_col] == 1
                        and (new_row, new_col) not in visited):

                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))
                        area+= 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    MaxArea = max(MaxArea, bfs(r,c))


        return MaxArea