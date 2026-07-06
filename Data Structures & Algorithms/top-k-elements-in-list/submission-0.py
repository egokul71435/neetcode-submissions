import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 6:55

        count = Counter(nums) # o(n)
        
        heap = []

        for num in count.keys(): # o(n)
            # push when space permits
            heapq.heappush(heap, (count[num], num)) # log(k)
            
            # otherwise remove smallest
            if len(heap) > k: 
                heapq.heappop(heap) # log(k)
        
        return [r[1] for r in heap] # o(n)

        # o(n log k) time; o(n + k) space

              