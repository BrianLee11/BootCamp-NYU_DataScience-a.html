# LeetCode Medium - 167 Two Sum II - Input Array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Topic: lists, arrays, sorting

"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, 
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.

Your solution must use only constant extra space.
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        type numers: List[int]
        type target: int
        rtype: List[int]
        """
        dictionary = {}

        for index in range(len(numbers)):
            complement = target - numbers[index]

            if complement in dictionary:
                return [dictionary[complement] + 1, index + 1]
            
            else:
                dictionary[numbers[index]] = index

        return False
