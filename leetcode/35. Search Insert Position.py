class Solution(object):
        def searchInsert(self, nums, target):
                """
                :type nums: List[int]
                :type target: int
                :rtype: int
                """
                pointer = 0
                while nums[pointer] < target and pointer <= (len(nums) - 1):
                        if pointer == len(nums) - 1:

                                return pointer + 1
                        else:
                                pointer += 1

                return pointer