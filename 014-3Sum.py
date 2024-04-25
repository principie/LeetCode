# Link: https://leetcode.com/problems/3sum/description/

# Brute force solution:
def threeSum(nums):
    triplets=[]
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i]+nums[j]+nums[k] == 0:
                    tri = sorted([nums[i],nums[j],nums[k]])
                    if tri not in triplets:                                 # Time Complexity: O(n^3)
                        triplets.append(tri)                                # Space Complexity: O(n^3)
    return triplets

nums1 = [-1,0,1,2,-1,-4]
nums2 = [-3,3,4,-3,1,2]
print(threeSum(nums2))


# Optimized sol:
 
def threeSum2(nums):
    triplets = []
    nums.sort()
    n = len(nums)

    for i , a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        l,r = i+1, n-1
        while l < r:
            sum = a + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                triplets.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:                           # Time Complexity: O(n^2)
                    l += 1                                                      # Space Complexity: O(1)
    return triplets

nums1 = [-1,0,1,2,-1,-4]
#nums2 = [-3,3,4,-3,1,2]
print(threeSum2(nums1))