class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        one=0
        two=0
        dr=(0,0,1,-1)
        dc=(1,-1,0,0)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    one+=1
                    for i in range(4):
                        nrow,ncol=row+dr[i],col+dc[i]
                        if 0<=nrow<len(grid) and 0<=ncol<len(grid[0]) and grid[nrow][ncol]==1:
                            two+=1
        #print(one,two)
        return one*4-two
                    