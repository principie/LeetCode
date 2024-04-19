# Link: https://leetcode.com/problems/palindrome-number/

# Brute Force:
def isPallindrome(x):
    if x < 0:
        return False
    else:
        return str(x) == str(x)[::-1]
    
x = 121
print(isPallindrome(x))             # Time Complexity: O(n)
                                    # Space Complexity: O(n)



# Another Solution:

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            if x // div != x % 10: return False             
            x = (x % div) // 10
            div = div / 100                       
        return True                             # Time Complexity: O(n)
                                                # Space Complexity: O(n)