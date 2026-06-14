class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start_time,end_time = intervals[0]
        print(start_time,end_time)
        print(intervals)
        res = []
        for i in range(1,len(intervals)):
            st,et = intervals[i]
            if st > end_time:
               res.append([start_time,end_time])
               start_time=st
               end_time=et
            else:
                if st <= end_time and et <=end_time:
                    start_time=start_time
                    end_time=end_time
                elif st <=end_time and et > end_time:
                    start_time=start_time
                    end_time=et 
        if res:            
            # print(res[-1],end_time)
            if res[-1][1] < start_time:
                # print('hi')
                res.append([start_time,end_time])
        else:
            res = [[start_time,end_time]]
        return res