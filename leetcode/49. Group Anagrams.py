import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        answer=collections.defaultdict(list)
        count=0
        for index, word in enumerate(strs):
                answer[str(sorted(word))].append(word)
        return answer.values()
strs=["eat", "tea", "tan", "ate", "nat", "bat"]
abc=Solution()
answer=abc.groupAnagrams(strs)
print(answer)