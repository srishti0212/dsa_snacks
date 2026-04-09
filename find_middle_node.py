def find_middle_node(head):
    slowpointer = head
    fastpointer = head 
    while fastpointer is not None and fastpointer. next is not None:
           fastpointer = fastpointer.next.next
           slowpointer = slowpointer.next
    return slowpointer


class Node:       
    def __init__(self, value):
        self.value = value
        self.next = None
   
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)    
        if self.head is None:
            self.head = new_node
            return 
        curr = self.head
        while curr.next is not None:
                curr = curr.next
        curr.next = new_node
 
def main():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print(find_middle_node(ll.head).value)

if __name__ == "__main__":
    main()