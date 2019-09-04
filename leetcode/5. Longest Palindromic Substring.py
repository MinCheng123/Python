class Solution(object):
        def longestPalindrome(self, s1):
                """
                :type s: str
                :rtype: str
                """
                if len(s1) == 0:
                        return s1
                if len(s1) == 1:
                        return s1
                if len(s1) == 2:
                        if s1[0] == s1[1]:
                                return s1
                        else:
                                return s1[0]
                length_odd = 1
                for i in range(len(s1)):
                        p1 = p2 = i
                        length_temp = 1
                        while p1 >= 0 and p2 < len(s1) and s1[p1] == s1[p2]:

                                if length_temp >= length_odd:
                                        length_odd = length_temp
                                        p1_f = p1
                                        p2_f = p2
                                p1 -= 1
                                p2 += 1
                                length_temp += 2

                length_even = 2
                flag = 0
                for j in range(len(s1)):
                        p3 = j
                        p4 = j + 1
                        length_temp = 2
                        while p3 >= 0 and p4 < len(s1) and s1[p3] == s1[p4]:
                                flag = 1
                                if length_temp >= length_even:
                                        p3_f = p3
                                        p4_f = p4
                                        length_even = length_temp

                                p3 -= 1
                                p4 += 1
                                length_temp += 2
                if flag == 0:
                        length_even = 0
                if length_odd > length_even:
                        return s1[p1_f:p2_f + 1]
                else:
                        return s1[p3_f:p4_f + 1]