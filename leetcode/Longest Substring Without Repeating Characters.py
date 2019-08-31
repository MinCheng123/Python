class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=[]
        if len(s)==0:
            return 1
        
        for i in range(len(s)):
            temp=[]
            for j in s[i:]:
                if j not in temp:
                    temp.append(j)
                else:
                    break
            if len(temp)> len(ans):
                ans=temp
        return len(ans)
s=" "
b=""
ans=Solution()
print(ans.lengthOfLongestSubstring(s))