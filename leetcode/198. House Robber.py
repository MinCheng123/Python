class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        
        pointer=2
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0]>nums[1]:
                return nums[0]
            else:
                return nums[1]
        if nums[1]<nums[0]:
            nums[1]=nums[0]
        while True:
            if pointer <= len(nums)-1:
                nums[pointer]= max( nums[pointer-2]+nums[pointer],nums[pointer-1]) 
            else:
                break
            pointer+=1
        return nums[-1]
            

abc=[1,3,1]
ABC=Solution()
answer=ABC.rob(abc)
print(answer)