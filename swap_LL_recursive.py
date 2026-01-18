
class Node(object):
    value: int
    next: 'Node'

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Solution(object):

    def swapHelper(self, prev, first):
        if not first or not first.next:
            return
        
        second = first.next
        third = second.next  
        
        second.next = first
        first.next = third
        prev.next = second

        return self.swapHelper(first, first.next)

    def swapConsecutiveElements(self, head):
        if not head or not head.next:
            return head

        dummy = Node(0, None)
        dummy.next = head
        prev = dummy

        self.swapHelper(prev, prev.next)

        return dummy.next

    # Define testcase as a method within the class
    def testcase(self, input, expectedList):
        actualOutput = self.swapConsecutiveElements(input)
        if expectedList == actualOutput:
            return print('test case successful')
        else:
            return print(actualOutput.value)

    def testsuite(self):
        
        #test case #1
        self.testcase(None, None) 

        #test case #2
        n1 = Node(1, None)
        self.testcase(n1, n1)

        #test case #3
        n4 = Node(4, None)
        n3 = Node(3, n4)
        n2 = Node(2, None)
        n1 = Node(1, n2)
        self.testcase(n1, n2)

        return

# Main part of the script
sol = Solution()
sol.testsuite() 


