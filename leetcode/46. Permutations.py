class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp=[]
        check=[]
        answer=[]
        self.backtracking(temp,nums,check,answer)
        return answer

    def backtracking(self,temp,nums,check,answer):
        if len(temp)==len(nums):
            temp2=temp[:]
            answer.append(temp2)
            return
        
        for digits in nums:
            if digits not in check:
                
                check.append(digits)
                temp=temp+[digits]
                self.backtracking(temp,nums,check,answer)
                temp.remove(digits)
                check.remove(digits)
        
        
nums=[1,2,3]
abc = Solution()
answer=abc.permute(nums)
print(answer)