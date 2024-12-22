# LeetCode - Medium - 283 - Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/
# Topic: lists, arrays, sorting

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [0] * len(nums)
        prefix[0] = 1

        for index in range(1, len(prefix)):
            prefix[index]  = nums[index - 1] * prefix[index - 1]

        postfix = [0] * len(nums)
        postfix[len(postfix) - 1] = 1

        for index in range(len(prefix) - 2, -1 , -1):
            postfix[index] = postfix[index + 1] * nums[index + 1]

        multiple = [0] * len(nums)

        for index in range(len(multiple)):
            multiple[index] = prefix[index] * postfix[index]

        return multiple