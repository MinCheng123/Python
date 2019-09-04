class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        i=0
        value=0
        answer=[]
        List=[]
        self.recursive(candidates,value,answer,List,target)
        return answer

    def recursive(self,candidates,value,answer,List,target):

        if value < target:
            for index, element in enumerate(candidates):
                    

                    self.recursive(candidates[index:],value+element,answer,List+[element],target)

        elif value == target:
            answer.append(List)
        else:
            return

Candidates=[2,3,6,7]
target = 7
abc=Solution()
answer=abc.combinationSum(Candidates,target)
print(answer)