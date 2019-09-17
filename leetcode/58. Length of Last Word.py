class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        count=0
        new_word=True
        old_count=0
        for element in s:

            if element == ' ':
                new_word=False
                count=0
            else:
                new_word=1
                count+=1
            if new_word==True: 
                old_count =count   
        return old_count