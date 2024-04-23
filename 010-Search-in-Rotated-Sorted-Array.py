# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

def search(nums, target: int):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        
        if nums[start] <= nums[mid]:
            if target > nums[mid] or target < nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if target < nums[mid] or target > nums[end]:
                end = mid - 1
            else:
                start = mid + 1

    return -1 

nums1 = [4,5,6,9,0,1,2]
print(search(nums1,2))

'''
Time Complexity: O(log n)
Space Complexity: O(1)
'''