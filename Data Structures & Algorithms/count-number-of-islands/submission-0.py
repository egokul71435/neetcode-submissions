class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def helper(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            helper(i+1,j)
            helper(i-1,j)
            helper(i,j+1)
            helper(i,j-1)
        
        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    counter += 1
                    helper(i, j)
        
        return counter
    
    # O(nm) time; finite num of accesses on each i,j
    # O(nm) space; call stack
