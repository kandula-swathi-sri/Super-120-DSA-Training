class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x:x[1])
        prev_endtime = intervals[0][1]
        minimum_remove = 0

        print(intervals)
        for a in range(1,n):
            current_start_time = intervals[a][0]
            if current_start_time>=prev_endtime:
                prev_endtime = intervals[a][1]
            else:
                minimum_remove+=1
        return minimum_remove
