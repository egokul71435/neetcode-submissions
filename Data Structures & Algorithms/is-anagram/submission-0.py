class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # 7:46

        # solution 1:

        return Counter(s) == Counter(t)

        # o(n) time; o(n) space

        # solution 2:

        # s_map = {}
        # for ch in s:
        #     s_map[ch] = s_map.get(ch, 0) + 1
        # t_map = {}
        # for ch in t:
        #     t_map[ch] = t_map.get(ch, 0) + 1

        # for k, v in s_map.items():
        #     if k not in t_map or t_map[k] != v:
        #         return False
        
        # return True

        # o(n) time; o(n) space
        