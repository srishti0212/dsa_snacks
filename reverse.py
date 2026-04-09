class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def reverseLL(self, head):
        current = head
        if current is None or current.next is None:
            return current
        
        dummy = None

        while current is not None:
           next_node = current.next
           current.next = dummy
           dummy = current
           current = next_node
        return dummy

    sol = Solution
    node1 = Node(1, None)
    node2 = Node(2,node1)
    node3 = Node(3, node2)
    node4 = Node(4, node3)
    self.reverseLL(node1)