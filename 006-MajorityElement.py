#Link: https://leetcode.com/problems/majority-element/

# Checking the numbers--
def majorELement(nums):
    n = len(nums)

    for i in nums:
        count = 0
        for j in range(n):
            if nums[j] == i:
                count += 1
        
        if count > n // 2:                          # Time Complexity: O(n^2)
            return i                                # Space Complexity: O(1)
                    
nums1 = [8,6,5,6,6]
print(majorELement(nums1))


# Using HashMap
def majorElement2(nums):
    count = {}

    for i in nums:
        count[i] = count.get(i, 0) + 1
        if count[i] > len(nums) //2:                # Time & Space complexity: O(n)
            return i

nums1 = [3,3,2,1,3,3]                                             
print(majorElement2(nums1))


# Moore's Voting Algorithm 
def majorElement3(nums):
    count, candidate = 0, None

    for i in nums:
        if count == 0:
            candidate = i
        count += (1 if i == candidate else -1)
    return candidate

nums1 = [3,3,2,1,3,3]                                           # Time complexity: O(n)   
print(majorElement3(nums1))                                     # Space complexity: O(1)