# Link: https://leetcode.com/problems/contains-duplicate/
-------------------------------------------------------------------------------------------------------------------------------------------------------
# Brute Force Approach:
def containsDuplicate_brute_force(nums):
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    
    return False


nums = [1, 2, 3, 1]
print(containsDuplicate_brute_force(nums))    ''' The time complexity of this approach is O(n^2) because we have two nested loops, 
                                                  and the space complexity is O(1) since we don't use any additional space.'''
-------------------------------------------------------------------------------------------------------------------------------------------------------
# 2nd Approach:
def containsDuplicate_sorting(nums):
    nums.sort()
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    
    return False

nums = [1, 2, 3, 1]
print(containsDuplicate_sorting(nums))     '''Time Complexity: Sorting the list takes O(n log n) time complexity.
                                              Space Complexity: Sorting the list can be done in-place, so the space complexity is O(1) for the sorting.'''

-------------------------------------------------------------------------------------------------------------------------------------------------------
# Optimized Approach:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False       '''The time complexity of the optimized approach is O(n), where n is the number of elements in the list nums,
                                because we iterate through the list only once. The space complexity is also O(n) in the worst case'''



def containsDuplicate_sorting(nums):
    nums.sort()
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    
    return False

nums = [1, 2, 3, 1]
print(containsDuplicate_sorting(nums))