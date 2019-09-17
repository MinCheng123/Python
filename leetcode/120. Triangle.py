class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        i=0
        index=0
        value =0
        self.recursive(triangle,index,i,value)
        return min(i)
        
    def recursive(self,List,index,i,value):
        if index==len(List)-1: 
            i.append(value)
#        value+= min(List[index][i], List[index][i+1]) 
#        i=List[index].index( min(List[index][i], List[index][i+1]))
        value+=self.recursive(List[index+1],i,value+List[index+1][i])
        value+=self.recursive(List[index+1],i+1,value+List[index+1][i+1])
triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]
abc=Solution()
answer=abc.minimumTotal(triangle)