class Solution:
    def isPalindrome(self, s: str) -> bool:

        # string cleaning; no space, all lower, alphanum only

        s_clean = "".join(ch.lower() for ch in s if ch.isalnum())
        
        return s_clean == s_clean[::-1]

        # O(n) time; O(n) space
