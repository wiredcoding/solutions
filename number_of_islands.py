class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Time complexity : O(M×N)where M is the number of rows and N is the number of columns.
        # space complexity: worst case O(M×N) in case that the grid map is filled with lands 
        
        # validate the input
        
        if grid is None or len(grid) <= 0:
            return 0
        
        def check_neighbors(grid, row, column):
            print 'calling'
            stack = []
            
            stack.append([row, column])
            
            # dfs using stack
            while len(stack) > 0:
                element = stack.pop()
                
                new_row = element[0]
                new_column = element[1]
                
                grid[new_row][new_column] = '0'
                
                if new_row + 1 < len(grid) and grid[new_row + 1][new_column] == '1':
                    stack.append([new_row + 1, new_column])
                
                if new_row - 1 >= 0 and grid[new_row - 1][new_column] == '1':
                    stack.append([new_row - 1, new_column])
                    
                if new_column -1 >= 0 and grid[new_row][new_column - 1] == '1':
                    stack.append([new_row, new_column - 1])
                    
                if new_column+1 < len(grid[0]) and grid[new_row ][new_column + 1] == '1':
                    stack.append([new_row, new_column + 1])   
                    
        
        number_of_islands = 0
        # run through the grid
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1':
                    number_of_islands += 1
                    
                    # go though the neighbours to check how big is the island
                    check_neighbors(grid, row, column)
        
        return number_of_islands 
    
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Time complexity : O(M×N)where M is the number of rows and N is the number of columns.
        # space complexity: worst case O(M×N) in case that the grid map is filled with lands 
        
        # validate the input
        
        if not grid:
            return 0
        
        number_of_islands = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1':
                    self.check_neighbors(grid, row, column)
                    number_of_islands += 1
        return number_of_islands

    def check_neighbors(self, grid, row, column):
        if row<0 or column<0 or row>=len(grid) or column>=len(grid[0]) or grid[row][column] != '1':
            return

        grid[row][column] = '#'

        self.check_neighbors(grid, row+1, column)
        self.check_neighbors(grid, row-1, column)
        self.check_neighbors(grid, row, column+1)
        self.check_neighbors(grid, row, column-1)