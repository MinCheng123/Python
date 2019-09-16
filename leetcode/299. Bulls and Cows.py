class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull,cow=0,0
        p,q=0,0
        temp=0
        count=0
        secret,guess=list(secret),list(guess)
        while p<len(guess):
                if secret[p] == guess[p]:
                    bull+=1
                    count+=1
                    secret.pop(p)
                    guess.pop(p)
                else:
                    p+=1
        while q<len(guess):
            if guess[q] in secret:
                secret.remove(guess[q])
                cow+=1
            q+=1   
                
         
        return str('{}A{}B'.format(bull,cow))


secret = "1122"

guess = "2211"

abc=Solution()
answer=abc.getHint(secret,guess)
print(answer)