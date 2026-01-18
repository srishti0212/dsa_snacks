
class Node(object):
    value: int
    next: 'Node'

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Solution(object):

    def swapConsecutiveElements(self, head):
        if not head or not head.next:
            return head

        dummy = Node(0, None)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # swap
            first.next = second.next
            second.next = first
            prev.next = second

            # move prev
            prev = first

        return dummy.next

    # Define testcase as a method within the class
    def testcase(self, input, expectedList):
        actualOutput = self.swapConsecutiveElements(input)
        if expectedList == actualOutput:
            return print('test case successful')
        else:
            return print(actualOutput)

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
