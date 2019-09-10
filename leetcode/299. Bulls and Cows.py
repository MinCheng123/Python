class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull,cow=0,0
        p=0
        temp=0
        count=0
        while p<len(guess):
                
                if secret[p] == guess[p]:
                    bull+=1
                    count+=1
                elif guess[p] in secret :
                    if temp==guess[p]:
                        count+=1
                    if count<=2:
                        cow+=1  
                temp=guess[p]
                p+=1
                
         
        return str('{}A{}B'.format(bull,cow))
secret = "1123"

guess = "0111"

abc=Solution()
answer=abc.getHint(secret,guess)
print(answer)