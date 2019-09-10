class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p2=1
        count=1
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        temp=nums[0]
        while True:
            if p2>len(nums)-1:
                break
            
            if temp ==nums[p2]:
                p2+=1     
            else:

                nums[count]=nums[p2]
                count+=1
                temp=nums[p2]
        return count
                