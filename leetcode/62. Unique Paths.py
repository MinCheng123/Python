class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        table = [[1 for i in range(m)] for j in range(n)]
        if m==1 and n>1:
            table=[[1 for i in range(n)]]
        elif n==1 and m>1:
            table=[[1] for j in range(m)]
        else:
            table = [[1 for i in range(n)] for j in range(m)]
            for i in range(1,m):
                for j in range(1,n):
                    table[i][j]=table[i-1][j]+table[i][j-1]
        return table[m-1][n-1]