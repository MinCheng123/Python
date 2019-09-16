import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer=[]
        List=collections.defaultdict(int)
        for i in nums:         
            List[i]+=1
            if List[i]> int(len(nums)/3):
                if i not in answer:
                    answer.append(i)
        return answer