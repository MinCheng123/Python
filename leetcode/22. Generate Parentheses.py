class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l,r=n,n
        answer=[]
        sub=''
        self.backtracking(l,r,sub,answer)
        return answer
        
    def backtracking(self,l,r,sub,answer):
        if l==0 and r == 0:
            answer.append(sub)
            return
        if l > r:
            return

            
        if l >0:
            self.backtracking(l-1,r,sub+'(',answer)
        if r >0:
            self.backtracking(l,r-1,sub+')',answer)

abc=Solution()
abc.generateParenthesis(3)