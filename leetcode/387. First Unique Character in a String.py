class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap={}
        i=0
        temp=100000000

        for index,element in enumerate(s):
            if element not in hashmap:
                hashmap[element]=[i,0,index]
                i+=1
            else:
                hashmap[element][1]+=1
        
        for index_hash, key in enumerate(hashmap):
            if hashmap[key][1]==0:
                if temp>hashmap[key][2]:
                    temp=hashmap[key][2]
        if temp==100000000:
            return -1
        return temp
