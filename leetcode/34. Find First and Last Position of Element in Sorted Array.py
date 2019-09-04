class Solution(object):
        def searchRange(self, nums, target):
                """
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
                """
                abc = []
                for index, i in enumerate(nums):
                        if i == target:
                                abc.append(index)
                if len(abc) == 0:
                        return [-1, -1]
                else:
                        if len(abc) == 1:
                                return [abc[0], abc[0]]
                        else:
                                return [abc[0], abc[-1]]
