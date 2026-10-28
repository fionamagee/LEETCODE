class Solution(object):
    def merge(self, intervals):
        if intervals == []:
            return []

        intervals.sort()

        output = [intervals[0]]
        left = 0
        for i in range(1,len(intervals)):
            if output[left][1] >= intervals[i][0]:
                output[left][1] = max(output[left][1], intervals[i][1])
            else:
                left += 1
                output.append(intervals[i])
        
        return output


        
