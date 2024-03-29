class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x >= 0 else -1
        new_x, x = 0, abs(x)
        while x>1:
            new_x = int(10*int( new_x) + x % 10)
            x /= 10
        new_x = flag * new_x
        return new_x if new_x < 2147483648 and new_x >= -2147483648 else 0