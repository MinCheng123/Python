class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) is 0:
            return []
        coordinate=[]
        for x in [0,len(board[0])-1]:
            for y in range(len(board)):
                if board[y][x] =='O':
                    self.backtracking(x,y,board,coordinate)
        for y in [0,len(board)-1]:
            for x in range(len(board[0])):
                if board[y][x] =='O':
                    self.backtracking(x,y,board,coordinate)
        for y in range(len(board)):
            for x in range(len(board[0])):
                if [x,y] not in coordinate and board[y][x] =='O':
                    board[y][x] ='X'
        
        return board
            
            
            
    def backtracking(self,x,y,board,coordinate):
        if board[y][x] =='O' and [x,y] not in coordinate:

            coordinate.append([x,y])
        
            if x+1<len(board[0]):
                self.backtracking(x+1,y,board,coordinate)
            if x-1>=0:
                self.backtracking(x-1,y,board,coordinate)
            if y+1<len(board):

                self.backtracking(x,y+1,board,coordinate)
            if y-1>=0:
                self.backtracking(x,y-1,board,coordinate)
            
                

grid=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

abc=Solution()
abc.solve(grid)