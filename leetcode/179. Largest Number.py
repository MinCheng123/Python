class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        string=''
        for i in range(len(nums)-1,-1,-1):
            for j in range(i):
                if not self.compare(nums[j],nums[j+1]):
                    nums[j+1],nums[j]=nums[j],nums[j+1]
        for k in nums:
            string+=str(k)
        if nums[0]==0:
            return '0'
        else:
            return string
        
    
    def compare(self,num1,num2):
        return str(num1)+str(num2)>str(num2)+str(num1)