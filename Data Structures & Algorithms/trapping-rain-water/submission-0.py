class Solution:
    def trap(self, height: List[int]) -> int:

        le_max, ri_max = [0] * len(height), [0] * len(height)

        l_max = r_max = 0

        for i in range(len(height)):
            le_max[i] = l_max
            l_max = max(l_max, height[i])
        
        for i in range(len(height) - 1, -1, -1):
            ri_max[i] = r_max
            r_max = max(r_max, height[i])
        
        res = 0 

        for i in range(len(height)):
            cur_water = min(le_max[i], ri_max[i]) - height[i]
            if cur_water > 0:
                res += cur_water
        
        return res
        




        