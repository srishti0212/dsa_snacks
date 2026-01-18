class Solution(object):

    def sort(self, width, height, length, mass):

        if None in (width, height, length, mass):
            return "REJECTED"
        
        if width<=0 or height<=0 or length<=0 or mass<=0:
            return "REJECTED"
        
        isBulky = width * height * length >= 1000000 or (width >= 150 or height >= 150 or length >= 150)
        isHeavy = mass >= 20
        
        if isHeavy and isBulky:
            return "REJECTED"
        elif isHeavy or isBulky:
            return "SPECIAL"
        else:
            return "STANDARD"


    def runTestSuite(self):
        self.testcase(None, None, None, None, "REJECTED") 
        self.testcase(0, 0, 0, 0, "REJECTED") 
        self.testcase(-1, 0, 0, 0, "REJECTED") 
        self.testcase(10, 10, 10, 10, "STANDARD") 
        self.testcase(150, 10, 10, 10, "SPECIAL") 
        self.testcase(10, 150, 10, 10, "SPECIAL") 
        self.testcase(10, 10, 150, 10, "SPECIAL") 
        self.testcase(10, 10, 10, 20, "SPECIAL") 
        self.testcase(10, 150, 10, 10000, "REJECTED")
        self.testcase(100, 100, 100, 10000, "REJECTED") 
        return 

    def testcase(self, w,h,l,m, expectedOutput):
        actualOutput = self.sort(w,h,l,m)
        if expectedOutput == actualOutput:
            return print('Test case successful', w,h,l,m, actualOutput, expectedOutput)
        else:
            return print('Test case Failed: ', w,h,l,m, actualOutput, expectedOutput)


s = Solution()
s.runTestSuite()