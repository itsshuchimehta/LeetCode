class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            # to get the end point of the first initialized interval
            lastEnd = output[-1][1]

            # check if the start of the next interval overlaps between current's end
            if start <= lastEnd:
                #Merge the inervals Note: Max() if the other's end < curr's end
                # [[1,5],[2,4]] = [1,5]
                output[-1][1] = max(lastEnd, end)
            else:
                # no Overlaping then just add it as it is 
                output.append([start,end]) 
        return output

