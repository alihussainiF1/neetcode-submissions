"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals = [[i.start,i.end] for i in intervals]
        intervals.sort()
        # print(intervals)
        start_time,end_time = intervals[0]

        for i in range(1,len(intervals)):
            st,et=intervals[i]
            if st<end_time :
                return False
            else:
                start_time = st
                end_time = et
        return True 
