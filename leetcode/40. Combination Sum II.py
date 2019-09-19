class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums=[]
        equal=[]
        check=[]
        List=[]
        answer=[]
        index=-1
        for i in candidates:
            if i < target:
                nums.append(i)
            elif i == target:
                equal.append([i])
        self.backtracking(nums,check,List,target, answer,index)
        answer.extend(equal)
        for i in range(len(answer)):
            answer[i]=sorted(answer[i])
       
        answer =  [list(x) for x in set([tuple(x) for x in answer])]


        return answer
        
            
    def backtracking(self,nums,check,List,target, answer,index):
        if sum(List) == target:
            temp=List[:]
            answer.append(temp)
            return
        elif sum(List) > target:
            return
        
        
        for i in range(len(nums)):
            if i>index:
                if i not in check:
                    index=i
                    check.append(i)
                    List.append(nums[i])
                    self.backtracking(nums,check,List,target, answer,index)
                    List.remove(nums[i])
                    check.remove(i)
                
target=1
candidates=[1,1]
abc=Solution()
answer=abc.combinationSum2(candidates,target)
print(answer)            