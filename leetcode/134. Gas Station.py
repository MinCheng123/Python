class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1

        sum_g,start,index=0,0,0
        
        length=len(gas)-1
        sum_g=gas[0]
        while True:
            if sum_g-cost[index] <0:
                index+=1
                start=index
                sum_g=gas[index]
            else:     
                if index>=length:
                    index_next=0
                else:
                    index_next=index+1

                sum_g+=gas[index_next]-cost[index]
                if sum_g<0:
                    start=index+1
                    sum_g=gas[index]
                else:   
                    if index_next==0:
                        index=0
                    elif index_next==-1:
                        index=-1
                    else:
                        index+=1
                if index==start:
                    return start

gas=[1,1,3]
cost=[2,2,1]
abc=Solution()
answer=abc.canCompleteCircuit( gas, cost)
print(answer)