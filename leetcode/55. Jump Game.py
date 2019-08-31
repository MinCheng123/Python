class Solution(object):
    def canJump(self, nums):
        end=len(nums)-2
        count=1
        while end != 0:
            if nums[end]>=count:
                count=1
                end-=1
            else:
                count+=1
                end-=1
        return nums[end]>=count        
            


nums=[2,0,0,0]               
Ans=Solution()
answer=Ans.canJump(nums)
print(answer)
            