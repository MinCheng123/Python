class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1:
            return 1
        answer=self.dp(n)
        return answer     
    
    def dp(self,n):
        List=[None for _ in range(n) ]
        
        List[0]=1
        List[1]=2
        for i in range(2,n):
            List[i]= List[i-1]+List[i-2]
        return List[-1]
n=35
abc=Solution()
answer=abc.climbStairs(n)
print(answer)