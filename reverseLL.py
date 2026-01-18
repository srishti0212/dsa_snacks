
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseLL(self, head):
        print('reversing')
        print(head.val, head.next.val, head.next.next.val)
        if head is None or head.next is None:
            return head

        dummy = Node(head.val, head)
        while head.next:
            temp = Node(head.next.val, dummy)
            dummy = temp
            head = head.next
        
        return dummy
        print(dummy.val, dummy.next.val, dummy.next.next.val)

    def testcase(self):
        tail = Node(3, None)
        b = Node(2, tail)
        head = Node(1, b)
        self.reverseLL(head)


sol = Solution()
sol.testcase() 
