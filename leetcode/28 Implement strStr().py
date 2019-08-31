class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ans=0
        flag=0
        complete=0
        if len(haystack)==0 and len(needle)==0:
            return 0
        if len(haystack)==0 or len(needle)>len(haystack) :
            return -1

        for index in range(len(haystack)):
           
                index_temp=index
                if len(haystack)-index >= len(needle):
                    for index2 in range(len(needle)):
                        if haystack[index_temp]== needle[index2]:
                            if flag==0:
                                ans=index
                            index2+=1
                            index_temp+=1
                            
                        else:
                            if flag==0:
                                ans=-1
                                break
                        if index2==len(needle):
                            complete=1
                    if complete==1:
                        flag=1
        return ans      
stack="aaa"
needle="a"

abc=Solution()
answer=abc.strStr(stack,needle)
print(answer)