class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left,right = n,n
        self.answer=[]
        temp=""
        self.recursive(left,right,temp) 
        return self.answer


    def recursive(self,left,right,temp):
        if not left and not right:
            self.answer.append("".join(temp))
            return 

        if  left:                
            temp = temp + "("
            left -= 1
            self.recursive(left,right,temp)     
        
        if right and left < right :
            temp = temp + ")"
            right -= 1
            self.recursive(left,right,temp)   
                        
    
        
        
abc=Solution()
answer = abc.generateParenthesis(3)
print(answer)
aaaaaaaaaaaaaaaaaaaaaaaaa