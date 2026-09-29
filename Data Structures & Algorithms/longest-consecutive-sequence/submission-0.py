class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort -> linear scan

        # populate set for all nums
        # linear scan, where if i-1 not in set, denotes start
        # search from this point

        num_set = set(nums)
        max_count = 0

        for n in nums:
            if n - 1 in num_set:
                continue
            else:
                curr_count = 1
                curr_num = n
                while curr_num + 1 in num_set:
                    curr_count += 1
                    curr_num += 1
                max_count = max(curr_count, max_count)
        
        return max_count

        # O(n) time; O(n) space