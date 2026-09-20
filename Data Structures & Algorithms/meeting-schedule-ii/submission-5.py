"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key = lambda x : x.start)
        heap = []

        if not intervals: return 0

        heapq.heappush(heap, intervals[0].end)
        rooms = 1

        for i in range(1, len(intervals)):

            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)
            
            else:
                rooms += 1
                heapq.heappush(heap, intervals[i].end)
        
        return rooms


        # initial incorrect solution

        # # sort -> continue on no conflict, new list otherwise
        # if not intervals:
        #     return 0

        # intervals.sort(key = lambda x : x.end)

        # ps, pe = intervals[0].start, intervals[0].end
        # rooms = 1

        # for i in range(1, len(intervals)):
        #     s, e = intervals[i].start, intervals[i].end

        #     if s < pe: # conflift:
        #         rooms += 1
        #     ps, pe = s, e
        
        # return rooms
            

        