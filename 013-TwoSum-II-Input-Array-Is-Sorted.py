# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

#Brute Force solution:

def twoSumII(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] + nums[j] == target:                                 # Time Complexity: O(n^2) 
                return [i+1, j+1]                                           # Space Complexity: O(1) 
            
nums1 = [2,7,11,15]
target = 9
print(twoSumII(nums1,target))

# -------------------------------------------------------------------------------------------------------------------------

# Better Solution:

def twoSum2(nums, target):
    num_map = {}

    for i, n in enumerate(nums):
        x = target - n
        if x in num_map:
            return [num_map[x], i+1]
        num_map[n] = i+1                                                         # Time Complexity: O(n)
    return[]                                                                     # Space Complexity: O(n)
nums1 = [2,7,11,15]                                                         
target = 9
print(twoSum2(nums1,target))

# -------------------------------------------------------------------------------------------------------------------------

def twoSum3(nums,target):
    l = 0
    r = len(nums)-1
    while l < r:
        res = nums[l] + nums[r]
        if res == target:
            return [l+1,r+1]
        
        if res > target:
            r -= 1                                                      # Time Complexity: O(n)
        else:                                                           # Space Complexity: O(1)
            l += 1

nums1 = [1,2,3,5,7,11,15]                                                         
target = 8
print(twoSum3(nums1,target))
