from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = 0

        for i in range(len(piles)):
            print(i)
            if piles[i] > maxPile: 
                maxPile = piles[i]
        
        l = 1
        r = ans = maxPile
        hours = 0 
        while l < r:
            mid = l + (r - l) // 2 
            for i in range(len(piles)):
                hours = hours + (piles[i] + mid -1 ) // mid
        
            if hours < h:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans



      # Define testcase as a method within the class
    def testcase(self, input1, input2, expectedList):
        actualOutput = self.minEatingSpeed(input1, input2)
        if expectedList == actualOutput:
            return print('test case successful', actualOutput)
        else:
            return print(actualOutput)

    def testsuite(self):
        
        #test case #1
        self.testcase([1,2,3,4,5,6], 6, 6) 

        # #test case #2
        # n1 = Node(1, None)
        # self.testcase(n1, n1)

        # #test case #3
        # n4 = Node(4, None)
        # n3 = Node(3, n4)
        # n2 = Node(2, None)
        # n1 = Node(1, n2)
        # self.testcase(n1, n2)

        return   


# Main part of the script
sol = Solution()
sol.testsuite() 

