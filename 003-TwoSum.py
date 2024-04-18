'''Brute Force Solution 
In the brute force approach, we can iterate through each element in the nums list and for each element, 
check if there exists another element in the list such that their sum equals the target. 
If such a pair is found, we return their indices. Here's the Python code for the brute force approach:
'''

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
nums = [2,1,5,3]
target = 4
print(two_sum(nums,target))


'''
Optimized Approach:
To optimize the solution, we can use a dictionary to store the elements of the list along with their indices.
While iterating through the list, we can check if the complement of the current element (i.e., target - nums[i]) 
exists in the dictionary. If it exists, we return the indices of the current element and its complement.
This approach reduces the time complexity to O(n) by sacrificing some additional space.
Here's the Python code for the optimized approach:
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


'''
Both approaches should give the same output [0, 1], but the optimized approach has a time complexity of O(n)
and a space complexity of O(n),whereas the brute force approach has a time complexity of O(n^2) and a space complexity of O(1).
'''