class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        summation=0
        answer=[]
        List=[]
        temp_index=0
        self.backtracking(candidates,target,summation,answer,List,temp_index)
        return answer
    
    def backtracking(self,candidates,target,summation,answer,List,temp_index):
        if summation > target:
            return
        elif summation == target:
            answer.append(List)
            
        for index,i in enumerate(candidates):
            
            if index>=temp_index:
                temp_index=index
                self.backtracking(candidates,target,summation+i,answer,List+[i],temp_index)

Candidates=[2,3,6,7]
target = 7
abc=Solution()
answer=abc.combinationSum(Candidates,target)
print(answer)