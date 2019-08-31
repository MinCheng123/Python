class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        size=len(matrix[0])
        
        for row, element in enumerate(matrix):
            for column, value in enumerate(element):
                if column != row and column < row:
                    matrix[row][column],matrix[column][row] = matrix[column][row],matrix[row][column]
        
        if size%2 != 0:
            for row, element in enumerate(matrix):
                for column, value in enumerate(element):
                    if column > (size-1)/2:
                        matrix[row][int(column-(column-(size-1)/2)*2)], matrix[row][column]=matrix[row][column],matrix[row][int(column-(column-(size-1)/2)*2)]
        else:
            for row, element in enumerate(matrix):
                for column, value in enumerate(element):
                    if column >= size/2:
                        matrix[row][int(column-(column-(size)/2)*2-1)], matrix[row][column]=matrix[row][column],matrix[row][int(column-(column-(size)/2)*2-1)]
        return matrix
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
abc=Solution()
ans=abc.rotate(matrix)
for element in matrix:
    print(element)