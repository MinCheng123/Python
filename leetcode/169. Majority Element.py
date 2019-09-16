import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        List=collections.defaultdict(int)
        for i in nums:         
            List[i]+=1
            if List[i]> len(nums)/3:
                return i
inp=[1,1,1,3,3,2,2,2]
abc=Solution()
answer=abc.majorityElement(inp)
print(answer)