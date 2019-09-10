class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        p=1
        p_temp=0
        count=2
        reset=1

        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        temp=nums[0]
        while True:
            if p>len(nums)-1:
                break     
            if temp ==nums[p]:
                p+=1
                reset+=1        
                if reset >=3:
                    nums.pop(p-1)
                    p-=1
            else:
                temp=nums[p]
                if reset==1:
                    count+=1
                else:
                    count+=2
                reset=1
                p+=1
        return count
nums = [0,0,1,1,1,1,2,3,3]
abc=Solution()
abc.removeDuplicates(nums)