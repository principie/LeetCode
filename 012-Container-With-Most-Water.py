#Link: https://leetcode.com/problems/container-with-most-water/description/

#Brute Force Solution:
def maxArea(nums):
    res = 0
    n = len(nums)
    for l in range(n):
        for r in range(l+1, n):
            area = (r - l) * min(nums[l], nums[r])
            res = max(area, res)                                    # Time Complexity: O(n^2)
    return res                                                      # Space Complexity: O(1)

nums1 = [1,8,6,2,5,4,8,3,7]
print(maxArea(nums1))


# Optimized Solution:
def maxArea1(nums):
    res = 0
    l, r = 0, len(nums) - 1

    while(l < r):
        area = (r - l) * min(nums[l], nums[r])
        res = max(area, res)

        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1                                              # Time Complexity: O(n)
                                                                # Space Complexity: O(1)
    return res

nums2 = [1,8,6,2,5,4,8,3,7]
print(maxArea1(nums2))