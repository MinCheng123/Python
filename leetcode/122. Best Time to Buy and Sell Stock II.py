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
        for index in range(len(prices)):
            if index == 0 or prices[index-1]==prices[index] and index!=len(prices)-1:
                if prices[index+1]>prices[index] and buy ==-1:
                    buy=prices[index]
                elif prices[index+1]<prices[index] and  buy!=-1:
                    profit+=prices[index]-buy
                    buy=-1
            elif index == len(prices)-1:
                if buy!=-1:
                    profit+=prices[-1]-buy            
            elif prices[index+1]>prices[index] and prices[index-1]>prices[index] and buy==-1:
                buy=prices[index]
            
            elif prices[index+1]<prices[index] and prices[index-1]<prices[index] and buy!=-1:
                profit+=prices[index]-buy
                buy=-1
        return profit

prices=[0,5,5,6,2,1,1,3]
abc=Solution()
answer=abc.maxProfit(prices)
            
