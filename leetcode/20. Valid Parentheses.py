class Solution(object):
        def isValid(self, s):
                """
                :type s: str
                :rtype: bool

                """
                abcd = []
                hashmap1 = {'(': ')', '{': '}', '[': ']'}
                hashmap2 = {')': '(', '}': '{', ']': '['}
                for element1 in s:
                        if element1 in hashmap1.keys():
                                abcd.append(hashmap1[element1])
                        if element1 in hashmap2.keys() and len(abcd) == 0:
                                return False
                        elif element1 in hashmap2.keys():
                                if abcd.pop(-1) != element1:
                                        return False
                if len(abcd) != 0:
                        return False
                else:
                        return True
