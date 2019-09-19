class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer,subset=[],[]
        self.backtracking(nums,0,answer,subset)
        return answer
        
    def backtracking(self,nums,start,answer,subset):
        answer.append(list(subset))
        for i in nums[start:]:
            subset.append(i)
            self.backtracking(nums,start+1,answer,subset)
            subset.pop()

nums = [1,2,3]
abc=Solution()
abc.subsets(nums)