class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_elements(head: ListNode, k: int) -> ListNode:
    current = dummy = ListNode(0, head)
    while current.next:
        if current.next.val == k:
            current.next = current.next.next
        else :
            current = current.next
    return dummy.next

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(1)
l4 = ListNode(1)
l5 = ListNode(2)
l6 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l = remove_elements(l1, 1)
while l:
    print(l.val)
    l = l.next

