class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ch_map = {}
        res = 0
        l = 0

        for r in range(len(s)):
            ch = s[r]
            if ch in ch_map:
                l = max(l, ch_map[ch] + 1)
            ch_map[ch] = r

            res = max(res, r - l + 1)

        return res

    # O(n) time; O(n) space