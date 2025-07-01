#
# https://neetcode.io/problems/is-palindrome?list=neetcode150
#

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right:
                if ord(s[left].lower()) in range(97, 123) or ord(s[left].lower()) in range(48, 58):
                    break
                left += 1
            
            while left < right:
                if ord(s[right].lower()) in range(97, 123) or ord(s[right].lower()) in range(48, 58):
                    break
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True
