class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    countS, countT = {}, {}

    for i in range(len(s)):
      countS[i] = 1 + countS.get(s[i], 0)
      countT[i] = 1 + countS.get(t[i], 0)
    for c in countS:
      if countS[c] != countT.get(c, 0):
        return False
      
    return True
  

''' Another solution
 return Counter(s) == Counter(t)
 or,
 sorter(s) == sorted(t)
 '''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}

        for c in s:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1

        for c in t:
            if c not in counter or counter[c] == 0:
                return False
            counter[c] -= 1

        return True

# Create an instance of the Solution class
solution = Solution()

# Define the input strings
s = "anagram"
t = "nagaram"

# Call the isAnagram method and print the result
print(solution.isAnagram(s, t))
