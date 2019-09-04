class Solution(object):
        def maxArea(self, height):
                """
                :type height: List[int]
                :rtype: int
                """
                area = 0
                j = 0
                i = len(height) - 1
                while i > j:
                        area = max(area, min(height[j], height[i]) * (i - j))
                        if height[i] > height[j]:
                                j += 1

                        else:
                                i -= 1
                return area
