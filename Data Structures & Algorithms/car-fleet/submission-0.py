class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [None] * len(position)

        for i in range(len(position)):
            pair[i] = (position[i], speed[i])
        
        pair.sort(reverse = True)
        stack = []

        for p, s in pair:
            time_to_reach = (target - p) / s

            # belongs to same fleet
            if stack and time_to_reach <= stack[-1]:
                continue
            # new fleet
            else:
                stack.append(time_to_reach)
        
        return len(stack)

        # O(nlogn) time; O(n) space