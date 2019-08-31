class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        history=[]
        ans=self.recursive(n,history)
        return ans
        
    def recursive(self,n,history):
        number=self.number(n)
        total=0
        for element in number:
            total=total + element**2
        if total==1:
            return True
        else:
            if total in history:
                return False
            else:
                history.append(total)
                flag=self.recursive(total,history)
                return flag
    
    def number(self,value):
        remainder=[]
        while value>=10:
            remainder.append(value%10)
            value=value-remainder[-1]
            value= int(value/10)
        remainder.append(value)
        return remainder[::-1]
n=19       
abc=Solution()
ans=abc.isHappy(n)
print(ans)