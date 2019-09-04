class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = g = -100000000000000
        for n in nums:
            l = max(n,l+n)
            g = max(l,g)
        return g
