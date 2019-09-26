class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        List=[i for i in range(1,10)]
        summation=0
        answer=[]
        visit=[]
        self.backtracking(List,summation,n,k,answer,visit)
        return answer
    
    def backtracking(self,List,summation,n,k,answer,visit):
        if summation==n:
            temp=visit
            answer.append(temp)
        if k ==0:
            return
        if summation>n:
            return
        
        
        for index, element in enumerate(List):
            if element not in visit:
                visit.append(element)
                self.backtracking(List[index:],summation+element,n,k-1,answer,visit)
                visit.pop()
abc=Solution()
answer=abc.combinationSum3( 3, 7)
print(answer)          