class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        List=[]
        for i in range(numRows):
            temp=[None for _ in range(i+1)]
            temp[0],temp[-1]=1,1
            
            for j in range(1,len(temp)-1):
                temp[j] =List[-1][j-1]+List[-1][j] 
            List.append(temp)
        return List