# Link: https://leetcode.com/problems/maximum-product-subarray/description/

#Brute Force sol:
def maxProduct(nums):
    maxP = float('-inf')
    n = len(nums)

    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j + 1):
                product *= nums[k]
                maxP = max(maxP, product)                           # Time Complexity: O(n^3)
                                                                    # Space Complexity: O(1)
    return maxP

nums1 = [2,3,-2,4]
print(maxProduct(nums1))
    
# Optimized Sol:
def maxProduct2(nums):
    res = max(nums)
    curMin, curMax = 1, 1

    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue
        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)                                           # Time Complexity: O(n)
    return res                                                           # Space Complexity: O(1)

nums2 = [2,3,-2,4]
print(maxProduct2(nums2))