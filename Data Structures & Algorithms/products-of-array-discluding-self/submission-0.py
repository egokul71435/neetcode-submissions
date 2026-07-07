class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 6:16

        res = [1] * len(nums)
        # prefix
        prefix = nums[0]
        for i in range(1, len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        # postfix
        postfix = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

        # o(n) time; o(n) space