# You are given an array of meeting time intervals:

# intervals = [[start1, end1], [start2, end2], ...]

# Return True if a person can attend all meetings (i.e., no overlaps), otherwise False.

class Solution():
    def main(self, intervals):
        intervals.sort(key = lambda x : x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True


# Main part of the script
sol = Solution()
stack = [[1,2], [2,4], [3,6]]
print(sol.main(stack))

