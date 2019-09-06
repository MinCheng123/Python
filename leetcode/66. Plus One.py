class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        

        flag=1
        for i in range(-1,-1-len(digits),-1):
                if flag+digits[i]==10 :
                    digits[i]=0
                    flag=1
                else:
                    digits[i] = digits[i] + flag
                    flag=0
        if flag==1: 
            digits.insert(0,1)  
        return digits