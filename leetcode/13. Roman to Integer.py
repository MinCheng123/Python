class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sub = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400 ,'CM':900}
        p=0
        value=0
        while p<len(s):
            if p<len(s)-1 and s[p]+s[p+1] in sub.keys():
                value+=sub[s[p]+s[p+1]]
                p+=2
            else:
                value+=dic[s[p]]
                p+=1
        return value