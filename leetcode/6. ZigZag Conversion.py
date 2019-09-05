class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        answer= ["" for i in range(numRows)]
        row = 0
        direction_flag = 0
        answer_final = ''
        if numRows ==1:
            return s
        for element in s:

            answer[row]=answer[row]+str(element)
            
            if row == numRows-1:
                flag =1
                
            if row == 0:
                flag =0
                
            if flag ==0:
                row+=1 
            else:
                row-=1
        answer_final = ''.join(answer)
        return    answer_final