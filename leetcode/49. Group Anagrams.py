import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        answer=collections.defaultdict(list)
        List=[]
        for index, word in enumerate(strs):
                answer[str(sorted(word))].append(word)
        for i in answer:
            List.append(answer[i])

        return List
strs=["eat", "tea", "tan", "ate", "nat", "bat"]
abc=Solution()
answer=abc.groupAnagrams(strs)
print(answer)