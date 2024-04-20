# Brute Force Approach:

def maxSubArray1(nums):
    max_sum = 0
    n = len(nums)

    for i in range(n):
        for j in range(i, n):
            curr_sum = sum(nums[i:j+1])
            max_sum = max(max_sum, curr_sum)                        # Time Complexity = O(n^3)
                                                                    # Space Complexity= O(n)
    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray1(nums))


# Better Approach:

def maxSubArray2(nums):
    maxSub = nums[0]
    curr_sum = 0

    for n in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n
        maxSub = max(curr_sum, maxSub)
    return maxSub

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]                               # Time Complexity = O(n)
print(maxSubArray2(nums))                                            # Space Complexity= O(1)


# Kadane's Algorithm:

def maxSubArray3(nums):
    max_sum, curr_sum = 0, 0

    for i in nums:
        curr_sum = max(i, curr_sum + i)
        max_sum = max(max_sum, curr_sum)
    return max_sum
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]                               # Time Complexity = O(n)
print(maxSubArray3(nums))                                            # Space Complexity= O(1)

