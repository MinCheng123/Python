class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
    
        count=0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    count+=1
                    self.dfs(grid,x,y)
                    
        return count
                
    def dfs(self, grid,x,y): 
        if grid[y][x] == '1':
            grid[y][x] = '0'
            if x+1<=len(grid[0])-1:  
                self.dfs(grid,x+1,y)
            if x-1>=0:
                self.dfs(grid,x-1,y)
            if y+1<= len(grid)-1:
                self.dfs(grid,x,y+1)
            if y-1 >=0:
                self.dfs(grid,x,y-1)
        else:
            return
grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
abc=Solution()
answer=abc.numIslands( grid)
print(answer)