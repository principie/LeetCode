# Link: https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for a in s:
            if a.isalpha() or a.isdigit():
                new += a.lower()                             # Time Complexity: O(n)
        return (new == new[::-1])                            # Space Complexity: O(n)
    

def isPallindrome2(s):
        new = ''
        for a in s:
            if a.isalnum():
                new += a.lower()
        return (new == new[::-1])                           #(Same)



def isPallindrome3(s):
     l,r = 0, len(s)-1

     while l < r:
          while l < r and not alphaNum(s[l]):
               l += 1
          while r < l and not alphaNum(s[r]):
               l -= 1
          if s[l].lower() != s[r].lower():
               return False
          l,r = l + 1, r -1 
     return True
    
def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

s = "aba"                                                       # Time Complexity: O(n) 
print(isPallindrome3(s))                                        # Space Complexity: O(1)