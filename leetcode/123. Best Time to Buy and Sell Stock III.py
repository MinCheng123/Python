class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==1:
            return 0
        buy=-1
        profit=0
        each_profit=[]
        for index in range(len(prices)):
            if index == 0 or prices[index-1]==prices[index] and index!=len(prices)-1:
                if prices[index+1]>prices[index] and buy ==-1:
                    buy=prices[index]
                elif prices[index+1]<prices[index] and  buy!=-1:
#                    profit+=prices[index]-buy
                   
                    each_profit.append(prices[index]-buy)
                    buy=-1
            elif index == len(prices)-1:
                if buy!=-1:
 #                   profit+=prices[-1]-buy  
                    each_profit.append(prices[index]-buy)
            elif prices[index+1]>prices[index] and prices[index-1]>prices[index] and buy==-1:
                buy=prices[index]
            
            elif prices[index+1]<prices[index] and prices[index-1]<prices[index] and buy!=-1:
#                profit+=prices[index]-buy               
                each_profit.append(prices[index]-buy)
                buy=-1
        for _ in range(2):
            profit+=max(each_profit)
            each_profit.remove(max(each_profit))
            
        return profit

prices=[1,2,4,2,5,7,2,4,9,0]
abc=Solution()
answer=abc.maxProfit(prices)