class Solution:

    def isSub(self, str, substr):
        totalWords = 0
        for item in substr:
            print('processing ', item)
            i = 0
            j = 0
            match = 0
            while j < len(item) and i < len(str):
                if item[j] == str[i]:
                    match += 1
                    j += 1
                    i += 1
                else:
                    i +=1
            if match == len(item):
                totalWords += 1
        return totalWords

    def testSuite(self):
        self.testcase('abcde', ['a','bb','ace','acd'], 3)
        self.testcase([''], ['a'], 0)
        self.testcase(['ade'], ['a','bb','ace','acd'], 0)
        
    def testcase(self,str, substr, exp):
        actual = self.isSub(str, substr)
        if exp == actual:
            print(s, exp, 'successful')
        else:
            print(s, exp, 'not successful')

s = Solution()
s.testSuite()