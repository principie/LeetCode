# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def findMin(nums):
    start, end = 0, len(nums) - 1

    while start < end:
        mid = (start + end) // 2

        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid

    return nums[start]                                                  # Time Complexity: O(log n)
                                                                        # Space Complexity: O(1)
nums1 = [3,4,5,1,2]
print(findMin(nums1))


