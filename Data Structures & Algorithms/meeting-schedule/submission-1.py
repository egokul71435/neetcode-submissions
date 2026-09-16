"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        intervals.sort(key=lambda x: x.start)

        ps, pe = intervals[0].start, intervals[0].end

        for i in range(1, len(intervals)):
            cs, ce = intervals[i].start, intervals[i].end
            if cs < pe:
                return False
            else:
                ps, pe = cs, ce
        
        return True

# O(nlogn) time; O(1) space
