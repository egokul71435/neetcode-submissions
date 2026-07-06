class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # 7:55

        r = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - 97] += 1
            

            if tuple(count) in r:
                r[tuple(count)].append(s)

            else:
                r[tuple(count)] = [s]
    
        return [v for k, v in r.items()]

        # o(nm) time; o(n) space
        