# LeetCode 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/
# Topic: lists, arrays, sorting
"""
Given an integer array nums, 
return true if any value appears at least twice in the array, and
return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        set_elements = set()

        for number in nums:
            if number in set_elements:
                return True
            else:
                set_elements.add(number)    

        return False

# testing
nums = [1,2,3,1]

solution = Solution()
result = solution.containsDuplicate(nums)
print(result)
