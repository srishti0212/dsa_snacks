'''

Given an integer array, check if it contains a contiguous subarray having zero-sum.

Input : [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
Output: True
Explanation: The subarrays with zero-sum are

[3, 4, -7]
[4, -7, 3]
[-7, 3, 1, 3]
[3, 1, -4]
[3, 1, 3, 1, -4, -2, -2]
[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

Input : [4, -7, 1, -2, -1]
Output: False
Explanation: The subarray with zero-sum doesn't exist.

'''
from typing import List

class Solution:
	def hasZeroSumSubarray(self, nums: List[int]) -> bool:
		s = set()
		s.add(0)
		total = 0
		
		for i in nums:
			print(s)
			total += i
			if total in s:
				return True
			s.add(total)
		return False
	

if __name__ == '__main__':
 
    nums = [4, -6, 3, -1, 4, 2, 7]
    s = Solution() 
    if s.hasZeroSumSubarray(nums):
        print('Sublist exists')
    else:
        print('Sublist does not exist')