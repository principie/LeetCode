# Link: https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import Counter
import heapq
 
def topKFrequent1(nums, k):
    counter = Counter(nums)
    heap = []
        
    for num, freq in counter.items():
        heapq.heappush(heap, (-freq, num))
        
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])                                   #Time Complexity: O(n logn)
                                                                                #Space Complexity: O(n)            
    return result

nums1 = [1,1,1,2,2,3] 
k = 2
print(topKFrequent1(nums1,k))


# ----------------------------------------------------------------------------------------------------------


def topKFrequent(nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:                                                   #Time Complexity: O(n)
                    return res                                                      #Space Complexity: O(n+k)
                
nums1 = [1,1,1,2,2,3] 
k = 2
print(topKFrequent(nums1,k))