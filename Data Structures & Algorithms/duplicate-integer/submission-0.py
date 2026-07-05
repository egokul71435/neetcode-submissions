class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 7:42

        s = set()

        for n in nums:
            if n in s:
                return True
            else:
                s.add(n)
        
        return False

        # o(n) time; o(n) space



