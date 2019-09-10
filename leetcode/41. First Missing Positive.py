class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        temp=1
        for element in nums:
            if element >=1:
                if temp == element:
                    temp+=1
                elif temp < element:            
                    return temp
        return temp

nums=[3,4,-1,1]
abc=Solution()
abc.firstMissingPositive(nums)