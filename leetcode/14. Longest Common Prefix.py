class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        else:
            for index,bokstav in enumerate(strs[0]) :
                for word in strs[1:]:
                    if  index>= len(word) or bokstav != word[index]:
                        return strs[0][:index]
        return strs[0]