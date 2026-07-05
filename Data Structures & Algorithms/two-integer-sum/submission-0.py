class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 7:52

        prev = {}

        for i, n in enumerate(nums):
            if (target - n) in prev:
                return [prev[target-n], i]
            else:
                prev[n] = i

        # o(n) time; o(n) space
        
        