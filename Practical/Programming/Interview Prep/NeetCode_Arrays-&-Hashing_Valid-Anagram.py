"""
https://neetcode.io/problems/is-anagram
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if both words are anagrams of each other

        Args:
            s (str): first word
            t (str): second word

        Returns:
            bool: True if they are anagrams, otherwise
                False
        
        INITIAL SOLUTION
        ```
        hashset_s = {}
        hashset_t = {}

        for i in s:
            if i not in hashset_s:
                hashset_s[i] = 1
            else:
                hashset_s[i] = hashset_s[i] + 1

        for j in t:
            if j not in hashset_t:
                hashset_t[j] = 1
            else:
                hashset_t[j] = hashset_t[j] + 1

        return hashset_s == hashset_t
        ```

        """

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        return countS == countT
